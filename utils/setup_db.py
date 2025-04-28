import sqlite3

def create_db():
    conn = sqlite3.connect('C:/Users/Standard User/OneDrive/Documents/IITJ/MTech/Sem4/VSCode_MTP/pdf_tags.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pdf_tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pdf_filename TEXT UNIQUE,
        unigram_tags TEXT,
        ngram_tags TEXT,
        corrected_tags TEXT,
        extracted_text TEXT
    )
    ''')


    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
