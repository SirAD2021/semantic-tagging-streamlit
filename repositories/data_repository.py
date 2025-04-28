import sqlite3

# def insert_pdf_tags(pdf_name, generated_tags, extracted_text):
#     conn = sqlite3.connect('C:/Users/Standard User/OneDrive/Documents/IITJ/MTech/Sem4/VSCode_MTP/pdf_tags.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     INSERT INTO pdf_tags (pdf_filename, generated_tags, extracted_text)
#     VALUES (?, ?, ?)
#     ''', (pdf_name, ",".join(generated_tags), extracted_text))

#     conn.commit()
#     conn.close()
def insert_pdf_tags(pdf_name, unigram_tags, ngram_tags, extracted_text):
    conn = sqlite3.connect('C:/Users/Standard User/OneDrive/Documents/IITJ/MTech/Sem4/VSCode_MTP/pdf_tags.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO pdf_tags (pdf_filename, unigram_tags, ngram_tags, extracted_text)
    VALUES (?, ?, ?, ?)
    ''', (pdf_name, ",".join(unigram_tags), ",".join(ngram_tags), extracted_text))

    conn.commit()
    conn.close()




# Function to update corrected tags later
def update_corrected_tags(pdf_filename, corrected_tags):
    conn = sqlite3.connect('pdf_tags.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pdf_tags
        SET corrected_tags = ?
        WHERE pdf_filename = ?
    ''', (', '.join(corrected_tags), pdf_filename))
    conn.commit()
    conn.close()



# def check_pdf_exists(pdf_name):
#     conn = sqlite3.connect('C:/Users/Standard User/OneDrive/Documents/IITJ/MTech/Sem4/VSCode_MTP/pdf_tags.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT generated_tags, corrected_tags, extracted_text FROM pdf_tags WHERE pdf_filename = ?', (pdf_name,))
#     row = cursor.fetchone()

#     conn.close()

#     if row:
#         return row  # (generated_tags, corrected_tags, extracted_text)
#     else:
#         return None
def check_pdf_exists(pdf_name):
    conn = sqlite3.connect('C:/Users/Standard User/OneDrive/Documents/IITJ/MTech/Sem4/VSCode_MTP/pdf_tags.db')
    cursor = conn.cursor()

    cursor.execute('SELECT unigram_tags, ngram_tags, corrected_tags, extracted_text FROM pdf_tags WHERE pdf_filename = ?', (pdf_name,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return row  # (unigram_tags, ngram_tags, corrected_tags, extracted_text)
    else:
        return None




# def search_pdfs_by_tag(tag_keyword):
#     conn = sqlite3.connect('pdf_tags.db')
#     cursor = conn.cursor()

#     query = '''
#         SELECT pdf_filename, generated_tags, corrected_tags
#         FROM pdf_tags
#         WHERE generated_tags LIKE ? OR corrected_tags LIKE ?
#     '''
#     like_pattern = f"%{tag_keyword}%"
#     cursor.execute(query, (like_pattern, like_pattern))
#     results = cursor.fetchall()

#     conn.close()
#     return results
def search_pdfs_by_tag(tag_keyword):
    conn = sqlite3.connect('C:/Users/Standard User/OneDrive/Documents/IITJ/MTech/Sem4/VSCode_MTP/pdf_tags.db')
    cursor = conn.cursor()

    query = '''
        SELECT pdf_filename, unigram_tags, ngram_tags, corrected_tags
        FROM pdf_tags
        WHERE unigram_tags LIKE ? OR ngram_tags LIKE ? OR corrected_tags LIKE ?
    '''
    like_pattern = f"%{tag_keyword}%"
    cursor.execute(query, (like_pattern, like_pattern, like_pattern))
    results = cursor.fetchall()

    conn.close()
    return results



def delete_pdf_entry(pdf_name):
    conn = sqlite3.connect('pdf_tags.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM pdf_tags WHERE pdf_filename = ?', (pdf_name,))

    conn.commit()
    conn.close()

    print(f"Deleted entry for PDF: {pdf_name}")