import fitz  # PyMuPDF

def fallback_extract_headings(pdf_path):
    doc = fitz.open(pdf_path)

    heading_font_size_threshold = 13  
    toc_page_skip = 2  # Skip first 2 pages 

    sections = {}
    last_heading = "Start"
    temp_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block["type"] == 0:  # text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        font_size = span["size"]

                        if not text:
                            continue

                        # Only start checking for headings after skipping ToC pages
                        if page_num >= toc_page_skip:
                            if font_size >= heading_font_size_threshold and text[0].isalpha():
                                # Detected a heading
                                if last_heading != "Start":
                                    sections[last_heading] = temp_text.strip()
                                    temp_text = ""

                                last_heading = text

                            else:
                                temp_text += " " + text

    # Save last collected text
    if last_heading and temp_text:
        sections[last_heading] = temp_text.strip()

    return sections
