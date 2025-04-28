from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_preliminaries(text):
    start_headers = ['Preliminary', 'Preliminaries', '0 Preliminaries', '1 Preliminaries', '1.1. Preliminaries']
    end_headers = ['Introduction', 'Theorem', 'Definition', 'Materials', 'Methods', 'Results', 'Conclusion', 'References']
    preliminaries = extract_section(text, start_headers, end_headers)
    return get_first_and_last_five_lines(preliminaries)
