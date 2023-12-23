
def cheetsheet():
    s = 'one two one two one'
    print(s.replace(' ', '-'))
    # one-two-one-two-one

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

#marks = ["：", ":", " - ", "(", "（"] # )
def any_str_in(marks, target):
    for mark in marks:
        if mark in target:
            return True
    return False

