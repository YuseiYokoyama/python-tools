
s = 'one two one two one'
print(s.replace(' ', '-'))
# one-two-one-two-one


marks = ["：", ":", " - ", "(", "（"] # )
def any_str_in(marks, target):
    for mark in marks:
        if mark in target:
            return True
    return False

