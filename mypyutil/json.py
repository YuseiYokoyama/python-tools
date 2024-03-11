import json

def _load(fname):
    #open(fname, encoding="utf_8_sig")
    return json.load(open(fpath, encoding="utf_8_sig"))

def save_to_file(data, fname):
    json.dump(data, open(fpath, "w", encoding="utf_8_sig"), indent=4, ensure_ascii=False)
