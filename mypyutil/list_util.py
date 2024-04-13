import math

def list_get(l, i, default=None):
    if i < len(l):
        return l[i]
    else:
        return default

def argmin(l):
    best_i = 0
    best_v = math.inf
    for i, v in enumerate(l):
        if v < best_v:
            best_i = i
            best_v = v
    return best_i

