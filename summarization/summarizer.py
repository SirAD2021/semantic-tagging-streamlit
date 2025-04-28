from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, min_length=150, max_length=300):
    chunk_size = 4000  # characters, safe for BART

    if len(text) <= chunk_size:
        summary = summarizer_pipeline(
            text,
            min_length=min(150, len(text) // 10),
            max_length=min(300, len(text) // 5),
            do_sample=False
        )[0]['summary_text']
        return summary
    else:
        summaries = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size]
            chunk_summary = summarizer_pipeline(
                chunk,
                min_length=min(150, len(chunk) // 10),
                max_length=min(300, len(chunk) // 5),
                do_sample=False
            )[0]['summary_text']
            summaries.append(chunk_summary)

        final_summary = " ".join(summaries)
        return final_summary
