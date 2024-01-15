import fitz # PyMuPDF

def get_text_from_pdf(fpath):
    doc = fitz.open(fpath)
    text = []
    for page in doc:
        _text = page.get_text()
        text.append(_text)
    text = "\n".join(text)
    #print("text") # debug
    #pp(text) # debug
    return text

