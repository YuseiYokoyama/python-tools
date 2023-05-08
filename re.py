import re

def any_pattern(target_list):
    seed = "|".join(map(re.escape, sorted(target_list, reverse=True)))
    #seed = "|".join(sorted(target_list, reverse=True))
    return re.compile(seed)

def replace(text, pattern):
    new = []
    bef = 0
    for m in pattern.finditer(text):
        start, end = m.span()
        new.append(text[bef:start])
        new.append("replaced")
        bef = end
    new.append(text[bef:])
    return "".join(new)

