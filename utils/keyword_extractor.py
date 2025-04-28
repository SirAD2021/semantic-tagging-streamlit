from .nlp_utils import extract_section, get_first_and_last_five_lines

# def extract_keywords(text):
#     start_headers = ['Keywords', 'Key words', 'keyword', 'Keyword']
#     end_headers = ['Introduction', '1.', 'I.', 'Categories', '1 Introduction', 'Acknowledgements']
#     keywords_section = extract_section(text, start_headers, end_headers)
#     return keywords_section.strip()


def extract_keywords(text):
    start_headers = ['Keywords', 'Key words', 'keyword', 'Keyword']
    end_headers = ['Introduction', '1.', 'I.', 'Categories', '1 Introduction',
                   'Acknowledgements', 'AMS', 'Subject Classification', 'DOI', 
                   'Received', 'Accepted', 'Department', 'School', 'University', 'E-mail']

    keywords_section = extract_section(text, start_headers, end_headers)

    # Hard limit: only take first 3-5 lines from extracted keywords_section
    lines = [line.strip() for line in keywords_section.split('\n') if line.strip()]
    limited_lines = lines[:5]  # Take only first 5 non-empty lines

    return '\n'.join(limited_lines).strip()