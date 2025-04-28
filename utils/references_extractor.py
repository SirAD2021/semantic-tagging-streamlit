from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_references(text):
    start_headers = ['References', 'REFERENCES']
    references = extract_section(text, start_headers)
    return get_first_and_last_five_lines(references)
