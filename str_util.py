
def cheetsheet():
    s = 'one two one two one'
    print(s.replace(' ', '-'))
    # one-two-one-two-one
    
    print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
    # One TwO One TwO One

    print(s.translate(str.maketrans({'o': 'XXX', 't': None})))
    # XXXne wXXX XXXne wXXX XXXne

    # 第一引数には置換元文字を連結した文字列、第二引数には置換先文字を連結した文字列、第三引数には削除する置換元文字列を連結した文字列を指定する。第三引数は省略可能。
    print(s.translate(str.maketrans('ot', 'OT', 'n')))
    # Oe TwO Oe TwO Oe

def get_before(text, phrase):
    i = text.find(phrase)
    if i == -1:
        raise ValueError(f"'{text}' has no '{phrase}'")
    return text[:i]

def get_after(text, phrase):
    i = text.find(phrase)
    if i == -1:
        raise ValueError(f"'{text}' has no '{phrase}'")
    i += len(phrase)
    return text[i:]

def get_inner(text, start, end):
    return text.split(start)[1].split(end)[0]

def get_common_head(text_left, text_right):
    text_common = []
    for l, r in zip(text_left, text_right):
        if l == r:
            text_common.append(l)
        else:
            break
    return "".join(text_common)

#marks = ["：", ":", " - ", "(", "（"] # )
def any_str_in(marks, target):
    for mark in marks:
        if mark in target:
            return True
    return False

