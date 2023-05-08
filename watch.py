from pprint import pprint as pp
from pprint import pformat as pf

import time

from toolwatch import LapTimer

def slow_func():
    time.sleep(0.01)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("This is hogehoge")
    args = parser.parse_args()

    size = 1000
    lap_timer = LapTimer(size, flg_out_stderr=True)
    for _ in range(size):
        lap_timer()
        slow_func()

    print('\33[32m' + 'end' + '\033[0m')

