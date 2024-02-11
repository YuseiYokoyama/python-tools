import functools
print = functools.partial(print, flush=True) # ref. https://qiita.com/HidKamiya/items/9e941a5389ba5eb79df1

print("print out to stderr", file=sys.stderr)
