
def read(fname):
    text = open(fpath, encoding="utf_8_sig").read()

    lines = open(fpath, encoding="utf_8_sig").readlines()
    lines = [l.strip() for l in lines]
    return lines


def read_big(fname):
    fname = "text.dat"
    with open(fname, encoding="utf_8_sig") as f:
        for line in f:
            line = line.strip()
            print('line', line) # debug

def w_l():
    open(fname, "w", encoding="utf_8_sig").write("\n".join(lines))

