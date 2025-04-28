# from repositories.data_repository import search_pdfs_by_tag

# def search_by_tag():
#     tag_keyword = input("\nEnter a keyword to search PDFs by tag: ").strip()

#     results = search_pdfs_by_tag(tag_keyword)

#     if not results:
#         print("\nNo PDFs found matching this keyword.")
#         return

#     print(f"\nPDFs matching keyword '{tag_keyword}':\n")

#     for pdf_filename, generated_tags, corrected_tags in results:
#         print(f"PDF: {pdf_filename}")
#         print(f"Generated Tags: {generated_tags}")
#         if corrected_tags:
#             print(f"Corrected Tags: {corrected_tags}")
#         print("-" * 40)

# if __name__ == "__main__":
#     search_by_tag()



























from repositories.data_repository import search_pdfs_by_tag

def search_by_tag():
    tag_keyword = input("\nEnter a keyword to search PDFs by tag: ").strip()

    results = search_pdfs_by_tag(tag_keyword)

    if not results:
        print("\nNo PDFs found matching this keyword.")
        return

    print(f"\nPDFs matching keyword '{tag_keyword}':\n")

    for pdf_filename, unigram_tags, ngram_tags, corrected_tags in results:
        print(f"\n---PDF---: \n{pdf_filename}")
        print(f"\n---Unigram Tags---: \n{unigram_tags}")
        print(f"\n---N-gram Tags---: \n{ngram_tags}")
        if corrected_tags:
            print(f"Corrected Tags: {corrected_tags}")
        print("-" * 40)

if __name__ == "__main__":
    search_by_tag()
