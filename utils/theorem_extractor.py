from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_theorem(text):
    start_headers = ['Theorem', 'Theorems', 'Important Theorems']
    end_headers = ['Definition', 'Preliminaries', 'Materials', 'Methods', 'Results', 'Discussion', 'Conclusion', 'References']
    theorem = extract_section(text, start_headers, end_headers)
    return get_first_and_last_five_lines(theorem)
