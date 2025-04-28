from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_tags(chunks, top_n=20):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(chunks)

    terms = vectorizer.get_feature_names_out()
    avg_tfidf_scores = tfidf_matrix.mean(axis=0).A1

    term_scores = sorted(zip(terms, avg_tfidf_scores), key=lambda x: x[1], reverse=True)

    top_tags = [term for term, score in term_scores[:top_n]]
    return top_tags

def get_ngram_tfidf_tags(chunks, top_n=20):
    try:
        vectorizer = TfidfVectorizer(ngram_range=(2, 3), stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(chunks)

        terms = vectorizer.get_feature_names_out()
        avg_tfidf_scores = tfidf_matrix.mean(axis=0).A1

        term_scores = sorted(zip(terms, avg_tfidf_scores), key=lambda x: x[1], reverse=True)

        top_ngram_tags = [term for term, score in term_scores[:top_n]]

        if not top_ngram_tags:
            return ["(No strong n-grams found)"]

        return top_ngram_tags

    except ValueError:
        return ["(No strong n-grams found)"]
