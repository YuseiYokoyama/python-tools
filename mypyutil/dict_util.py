def cheetsheet():
    d1 = {'k1': 1, 'k2': 2}
    d2 = {'k1': 100, 'k3': 3, 'k4': 4}
    d1.update(d2)
    print(d1)
    # {'k1': 100, 'k2': 2, 'k3': 3, 'k4': 4}
