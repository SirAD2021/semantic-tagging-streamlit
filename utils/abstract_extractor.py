# from .nlp_utils import extract_sections

# def extract_abstract(text):
#     headers = ["Abstract", "Introduction"]
#     sections = extract_sections(text, headers)
#     return sections["Abstract"]





























































































from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_abstract(text):
    start_headers = ['Abstract']
    end_headers = ['Introduction', 'Key words', 'Keywords', 'Acknowledgements', 'Proof', 'Theorem']
    abstract = extract_section(text, start_headers, end_headers)
    return get_first_and_last_five_lines(abstract)
