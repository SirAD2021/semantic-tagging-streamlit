# import fitz

# def extract_text_from_pdf(pdf_path):
#     text = ''
#     header_footer_threshold = 50  # points from top and bottom of page to exclude

#     with fitz.open(pdf_path) as doc:
#         for page in doc:
#             blocks = page.get_text("blocks")
#             page_height = page.rect.height

#             # filter out headers and footers
#             filtered_blocks = []
#             for b in blocks:
#                 _, y0, _, y1, block_text, _, _ = b
#                 # remove blocks near top/bottom (headers/footers)
#                 if y0 > header_footer_threshold and y1 < (page_height - header_footer_threshold):
#                     filtered_blocks.append((y0, block_text))

#             # sort blocks by vertical position (top to bottom)
#             filtered_blocks.sort(key=lambda block: block[0])
#             page_text = '\n'.join(block_text.strip() for _, block_text in filtered_blocks)
#             text += page_text + "\n"

#     return text










































































import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    header_footer_threshold = 50  # points from top and bottom

    toc_active = False
    last_y = 0
    toc_y_threshold = 7 * 72  # 7 inches max, about 500 points
    toc_gap_threshold = 200   # if vertical gap > 200 points, assume ToC ended

    for page_index, page in enumerate(doc):
        blocks = page.get_text("blocks")
        page_height = page.rect.height

        filtered_blocks = []

        for b in blocks:
            x0, y0, x1, y1, block_text, _, _ = b
            block_text = block_text.strip()

            if not block_text:
                continue

            # Remove headers and footers
            if y0 < header_footer_threshold or y1 > (page_height - header_footer_threshold):
                continue

            # Activate TOC skipping if "Contents" found
            if not toc_active and any(word in block_text.lower() for word in ["contents", "table of contents"]):
                toc_active = True
                last_y = y1
                continue  # Skip "Contents" title itself

            if toc_active:
                if y0 - last_y > toc_gap_threshold:
                    toc_active = False  # big vertical gap, ToC is over
                elif y0 < toc_y_threshold:
                    continue  # Still inside ToC vertical zone, skip
                else:
                    toc_active = False  # If below reasonable Y limit, assume ToC done

            # Normal block
            filtered_blocks.append((y0, block_text))
            last_y = y1

        # Sort blocks vertically
        filtered_blocks.sort(key=lambda block: block[0])
        page_text = '\n'.join(block_text for _, block_text in filtered_blocks)
        text += page_text + "\n"

    return text
