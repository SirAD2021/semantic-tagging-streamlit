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

