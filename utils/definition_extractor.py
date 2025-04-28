from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_definition(text):
    start_headers = ['Definition', 'Definitions']
    end_headers = ['Preliminaries', 'Theorem', 'Materials', 'Methods', 'Results', 'Discussion', 'Conclusion', 'References']
    definition = extract_section(text, start_headers, end_headers)
    return get_first_and_last_five_lines(definition)
