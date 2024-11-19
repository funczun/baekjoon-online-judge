# https://www.acmicpc.net/problem/5086

import sys

while True:
    first, second = map(int, sys.stdin.readline().strip().split())

    if (first, second) == (0, 0):
        break

    if first > second and first % second == 0:
        print("multiple")
    elif first < second and second % first == 0:
        print("factor")
    else:
        print("neither")