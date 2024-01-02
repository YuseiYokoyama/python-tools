import os
import glob

def cheetsheet():
    files = os.listdir(path)

    os.makedirs("any/path", exist_ok=True)

    os.path.exists(fpath)

    os.remove(fpath)
    shutil.rmtree(dirpath)

    if fpath.endswith(".xlsx"):
        pass

def use_glob(dirpath):
    targets = glob.glob(os.path.join(dirpath, "*.csv"))
    for fpath in targets:
        print('fpath', fpath) # debug

def get_basename(fpath):
    basename = os.path.basename(fpath)
    corename = os.path.splitext(os.path.basename(fpath))[0]
    changed = os.path.splitext(fpath)[0] + ".jpg"

def get_file_dir():
    dirname = os.path.dirname(__file__)

def my_makedirs(fpath):
    dirname = os.path.dirname(fpath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)



