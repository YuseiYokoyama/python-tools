def list_get(l, i, default=None):
    if i < len(l):
        return l[i]
    else:
        return default

