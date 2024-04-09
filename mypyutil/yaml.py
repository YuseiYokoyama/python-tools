import yaml

def load(fpath):
    data = yaml.safe_load(open(fpath))
    data = yaml.safe_load(open(fpath, encoding="utf_8_sig"))
    data = yaml.safe_load(open(fpath, encoding="utf-16"))

def write(fpath):
    yaml.dump(obj, open(fpath, "w"))
    yaml.dump(obj, open(fpath, "w", encoding="utf_8_sig"), allow_unicode=True)
    yaml.dump(obj, open(fpath, "w", encoding="utf-16"), allow_unicode=True)
