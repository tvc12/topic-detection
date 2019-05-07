from gensim.utils import simple_preprocess

def clean_text(text):
    process_text = simple_preprocess(text)
    process_text = ' '.join(process_text)
    return process_text

def preprocess_text(texts, tokenizer):
    tok_doc = []
    i = len(texts)
    for text in texts:
        if isinstance(text, str):
            text = clean_text(text)
            tok_txt = tokenizer.tokenize(text)
            tok_doc.append(tok_txt)
        print("Done ", i)
        i -= 1
    return tok_doc