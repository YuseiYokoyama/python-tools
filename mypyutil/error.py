import traceback

try:
    hoge
except Exception as e:
    print(traceback.format_exc())
else:
    print("no error")
