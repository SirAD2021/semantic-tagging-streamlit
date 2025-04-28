# from .nlp_utils import extract_sections

# def extract_introduction(text):
#     headers = ["Introduction", "Conclusion"]
#     sections = extract_sections(text, headers)
#     return sections["Introduction"]





























































































from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_introduction(text):
    start_headers = ['Introduction', '0 Introduction', '1 Introduction', 'I Introduction']
    end_headers = ['2 ', 'II', 'Materials', 'Methods', 'Results', 'Discussion', 'Conclusion', 'Acknowledgements', 'References', 'Proof', 'Theorem']
    intro = extract_section(text, start_headers, end_headers)
    return get_first_and_last_five_lines(intro)

