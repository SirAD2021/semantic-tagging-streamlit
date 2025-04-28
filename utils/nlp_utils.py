# import re

# def extract_sections(text, headers):
#     sections = {header: [] for header in headers}
#     current_section = None

#     # Prepare patterns to detect headers even within the same line as text
#     header_patterns = {
#         header: re.compile(
#             rf'^\s*(?:\d+\.?\s*)?{re.escape(header)}\s*[:.]?\s*(.*)$',
#             re.IGNORECASE
#         )
#         for header in headers
#     }

#     lines = text.split("\n")

#     for line in lines:
#         line_clean = line.strip()

#         # Check if the line contains a header
#         header_found = False
#         for header, pattern in header_patterns.items():
#             match = pattern.match(line_clean)
#             if match:
#                 current_section = header
#                 header_found = True
#                 remaining_text = match.group(1).strip()
#                 if remaining_text:
#                     sections[current_section].append(remaining_text)
#                 break  # stop after finding the header

#         if not header_found and current_section:
#             sections[current_section].append(line_clean)

#     # Summarize sections clearly
#     extracted_summary = {}
#     for section, content in sections.items():
#         content = [line for line in content if line]
#         first_five = "\n".join(content[:5]) if len(content) > 5 else "\n".join(content)
#         last_five = "\n".join(content[-5:]) if len(content) > 5 else "\n".join(content)
#         extracted_summary[section] = {
#             "first_five": first_five if first_five else "No content extracted",
#             "last_five": last_five if last_five else "No content extracted"
#         }

#     return extracted_summary




















































# import re
# import fitz

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text

# def extract_section(text, start_headers, end_headers=None):
#     if end_headers is None:
#         end_headers = []

#     start_pattern = '|'.join([rf'\b{re.escape(h)}\b\.?' for h in start_headers])
    
#     if end_headers:
#         end_pattern = '|'.join([rf'\b{re.escape(h)}\b\.?' for h in end_headers])
#         pattern = rf'(?:{start_pattern})(.*?)(?={end_pattern})'
#     else:
#         pattern = rf'(?:{start_pattern})(.*)'

#     match = re.search(pattern, text, flags=re.DOTALL | re.IGNORECASE)
    
#     return match.group(1).strip() if match else "No content extracted"

# def get_first_and_last_five_lines(section_text):
#     lines = [line.strip() for line in section_text.split('\n') if line.strip()]
#     first_five = lines[:5] if len(lines) >= 5 else lines
#     last_five = lines[-5:] if len(lines) > 5 else lines
#     return first_five, last_five





































































import re
import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_section(text, start_headers, end_headers=None):
    if end_headers is None:
        end_headers = []

    start_pattern = '|'.join([rf'\b{re.escape(h)}\b\.?' for h in start_headers])

    if end_headers:
        end_pattern = '|'.join([rf'\b{re.escape(h)}\b\.?' for h in end_headers])
        pattern = rf'(?:{start_pattern})(.*?)(?={end_pattern})'
    else:
        pattern = rf'(?:{start_pattern})(.*)'

    match = re.search(pattern, text, flags=re.DOTALL | re.IGNORECASE)
    section_text = match.group(1).strip() if match else "No content extracted"
    return remove_equation_lines(section_text)


    # # clearly filter out equations here
    # filtered_text = remove_equation_lines(section_text=section_text)
    # return filtered_text

def get_first_and_last_five_lines(section_text):
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    first_five = lines[:5] if len(lines) >= 5 else lines
    last_five = lines[-5:] if len(lines) > 5 else lines
    return first_five, last_five

def remove_equation_lines(section_text):
    import re
    equation_pattern = re.compile(r'^[\s\d\(\)\[\]\{\}.,;:=+\-*/^_\\<>&%$#@!|~]+$')

    lines = section_text.split('\n')
    filtered_lines = [line for line in lines if not equation_pattern.match(line.strip())]

    return '\n'.join(filtered_lines).strip()

