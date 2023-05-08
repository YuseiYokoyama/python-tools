import os
import glob

def use_glob(dirname):
    targets = glob.glob(os.path.join(dirname, "*.csv"))
    for fpath in targets:
        print('fpath', fpath) # debug

def get_basename(fpath):
    basename = os.path.basename(fpath)
    corename = os.path.splitext(os.path.basename(fpath))[0]
    changed = os.path.splitext(fpath)[0] + ".jpg"

def get_file_dir():
    dirname = os.path.dirname(__file__)

os.makedirs("any/path", exist_ok=True)

os.path.exists(fpath)

os.remove(fpath)

if fpath.endswith(".xlsx"):

