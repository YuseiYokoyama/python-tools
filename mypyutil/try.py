try:
    pass
except ZeroDivisionError:
    pass
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")

raise NotImplementedError("msg")

