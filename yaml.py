import yaml

def load(fpath):
    data = yaml.safe_load(open(fpath, encoding="utf_8_sig"))

def write(fpath):
    yaml.dump(obj, open(fpath, "w", encoding="utf_8_sig"), allow_unicode=True)
