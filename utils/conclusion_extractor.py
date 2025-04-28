from .nlp_utils import extract_section, get_first_and_last_five_lines

def extract_conclusion(text):
    start_headers = ['Conclusion', 'Conclusions', 'Conclusion.', 'CONCLUSION', 'CONCLUSIONS.', '1. Conclusion', '1.Conclusion', '2.Conclusion']
    end_headers = ['Acknowledgements', 'References']
    conclusion = extract_section(text, start_headers, end_headers)
    return get_first_and_last_five_lines(conclusion)
