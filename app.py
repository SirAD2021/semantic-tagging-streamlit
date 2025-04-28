import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.abstract_extractor import extract_abstract
from utils.introduction_extractor import extract_introduction
from utils.conclusion_extractor import extract_conclusion
from utils.references_extractor import extract_references
from utils.keyword_extractor import extract_keywords
from utils.text_chunker import get_chunks
from utils.tfidf_tagger import get_tfidf_tags, get_ngram_tfidf_tags
from repositories.data_repository import (
    insert_pdf_tags,
    update_corrected_tags,
    check_pdf_exists,
    delete_pdf_entry,
    initialize_database
)
from utils.preliminaries_extractor import extract_preliminaries
from utils.theorem_extractor import extract_theorem
from utils.definition_extractor import extract_definition
from utils.toc_cleaner import remove_table_of_contents
from summarization.summarizer import generate_summary
from transformers import pipeline

# Initialize database at app startup
initialize_database()

# Initialize summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Search PDFs by tag
def search_pdfs_by_tag(tag_keyword):
    conn = sqlite3.connect('pdf_tags.db')
    cursor = conn.cursor()

    query = '''
        SELECT pdf_filename, unigram_tags, ngram_tags, corrected_tags
        FROM pdf_tags
        WHERE unigram_tags LIKE ? OR ngram_tags LIKE ? OR corrected_tags LIKE ?
    '''
    like_pattern = f"%{tag_keyword}%"
    cursor.execute(query, (like_pattern, like_pattern, like_pattern))
    results = cursor.fetchall()

    conn.close()
    return results

st.set_page_config(page_title="Semantic Tagging and Summarization", layout="wide")

st.title("Semantic Tagging and Summarization System")

menu = ["Upload and Process PDF", "Search PDFs by Tag"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Upload and Process PDF":
    uploaded_pdf = st.file_uploader("Upload a research PDF file", type=["pdf"])

    if uploaded_pdf is not None:
        with st.spinner('Processing your PDF...'):
            with open("temp_uploaded.pdf", "wb") as f:
                f.write(uploaded_pdf.read())

            try:
                text = extract_text_from_pdf("temp_uploaded.pdf")
                text = remove_table_of_contents(text)

                abstract_first, abstract_last = extract_abstract(text)
                intro_first, intro_last = extract_introduction(text)
                conclusion_first, conclusion_last = extract_conclusion(text)
                references_first, references_last = extract_references(text)

                abstract_chunks = get_chunks("\n".join(abstract_first + abstract_last))
                introduction_chunks = get_chunks("\n".join(intro_first + intro_last))
                conclusion_chunks = get_chunks("\n".join(conclusion_first + conclusion_last))
                references_chunks = get_chunks("\n".join(references_first + references_last))

                all_chunks = abstract_chunks + introduction_chunks + conclusion_chunks + references_chunks

                st.success('PDF processed successfully.')

                st.header("Semantic Tags")

                unigram_tags = get_tfidf_tags(all_chunks, top_n=20)
                ngram_tags = get_ngram_tfidf_tags(all_chunks, top_n=20)

                st.subheader("Unigram Tags (Single Words)")
                if unigram_tags:
                    st.write(", ".join(unigram_tags))
                else:
                    st.write("(No meaningful unigrams found)")

                st.subheader("N-gram Tags (Phrases)")
                if ngram_tags and ngram_tags[0] != "(No strong n-grams found)":
                    st.write(", ".join(ngram_tags))
                else:
                    st.write("(No meaningful n-grams found)")

                st.header("Edit/Confirm Tags (Optional)")
                corrected_tags = st.text_area(
                    "Correct or re-enter tags (comma-separated):",
                    value=", ".join(unigram_tags),
                    height=150
                )

                if st.button("Save Tags to Database"):
                    pdf_name = uploaded_pdf.name
                    existing_entry = check_pdf_exists(pdf_name)

                    if existing_entry:
                        update_corrected_tags(pdf_name, [tag.strip() for tag in corrected_tags.split(",")])
                        st.success("Tags updated successfully in the database.")
                    else:
                        insert_pdf_tags(
                            pdf_name,
                            unigram_tags,
                            ngram_tags,
                            "\n".join(all_chunks)
                        )
                        st.success("New PDF entry and tags saved successfully to the database.")

                st.header("Generate Summary")
                if st.button("Generate Summary"):
                    full_text = "\n".join(all_chunks)
                    if full_text.strip():
                        summary = generate_summary(full_text, min_length=100, max_length=min(600, len(full_text) // 2))
                        st.subheader("Document Summary:")
                        st.success(summary)
                    else:
                        st.error("Document too small for summarization.")

            except Exception as e:
                st.error(f"An error occurred while processing the PDF: {e}")

    else:
        st.info("Please upload a PDF file to begin.")

elif choice == "Search PDFs by Tag":
    st.subheader("Search PDFs by Keyword Tag")

    tag_keyword = st.text_input("Enter a keyword to search PDFs:")

    if st.button("Search"):
        if tag_keyword.strip() != "":
            results = search_pdfs_by_tag(tag_keyword.strip())

            if results:
                st.success(f"Found {len(results)} matching PDFs:")
                for pdf_filename, unigram_tags, ngram_tags, corrected_tags in results:
                    st.write(f"**PDF:** {pdf_filename}")
                    st.write(f"**Unigram Tags:** {unigram_tags}")
                    st.write(f"**N-gram Tags:** {ngram_tags}")
                    if corrected_tags:
                        st.write(f"**Corrected Tags:** {corrected_tags}")
                    st.markdown("---")
            else:
                st.warning("No PDFs found matching this tag.")
        else:
            st.warning("Please enter a tag to search.")
