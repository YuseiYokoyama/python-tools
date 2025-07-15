from collections import Counter, defaultdict

whole = defaultdict(int)
whole = defaultdict(list)

def cheetsheet_for_counter():
    print(c.most_common()[0])
    # ('a', 4)

    print(c.most_common()[-1])
    # ('b', 1)

    print(c.most_common()[0][0])
    # a

    print(c.most_common()[0][1])
    # 4
