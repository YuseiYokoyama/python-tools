import os
import pickle
def deco_tag(tag):
    def _deco_tag(func):
        def wrapper(*args, **kwargs):
            res = '<'+tag+'>'
            res = res + func(*args, **kwargs)
            res = res + '</'+tag+'>'
            return res
        return wrapper
    return _deco_tag
