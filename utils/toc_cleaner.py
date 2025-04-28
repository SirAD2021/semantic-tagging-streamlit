import re

def remove_table_of_contents(text):
    toc_patterns = ['table of contents', 'contents']
    lower_text = text.lower()

    for toc_start in toc_patterns:
        idx = lower_text.find(toc_start)
        if idx != -1:
            text = text[idx + len(toc_start):]  # remove all before and including "contents"
            break

    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()

        # Skip typical TOC lines: short lines ending with numbers
        if len(line) < 100 and (line.endswith('1') or line.endswith('2') or line.endswith('3') or re.search(r'\d$', line)):
            continue

        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)
