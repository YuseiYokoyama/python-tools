from pprint import pprint as pp
from pprint import pformat as pf

from functools import wraps
import datetime


# usage: @my_logger
def my_logger(f):
    @wraps(f)
    def _wrapper(*args, **kwargs):
        # 前処理
        print(f'{f.__name__}の実行')
        print(f'開始: {datetime.datetime.now()}')

        # デコレート対象の関数の実行
        v = f(*args, **kwargs)

        # 後処理
        print(f'終了: {datetime.datetime.now()}')
        print(f'実行結果: {v}')

        return v
    return _wrapper

def log_arguments_on_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            out = {
                "func": func.__name__,
                "args": args,
                "kwargs": kwargs,
            }
            pp(out)
            raise e
    return wrapper

# usage: @tag("h1")
def html_tag(tag_name):
    def _deco(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):
            # 前処理
            v = f(*args, **kwargs)
            # 後処理
            return f'<{tag_name}>{v}</{tag_name}>'
        return _wrapper
    return _deco

# get arg by name
from inspect import getfullargspec
def decorator(argument_name):
    def _decorator(f):
        argspec = getfullargspec(f)
        argument_index = argspec.args.index(argument_name)
        @wraps(f)
        def wrapper(*args, **kwargs):
            if argument_index < len(args):
                value = args[argument_index]
            else:
                value = kwargs[argument_name]
            # do something with value
            return f(*args, **kwargs)
        return wrapper
    return _decorator

