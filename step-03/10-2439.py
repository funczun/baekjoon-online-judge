# https://www.acmicpc.net/problem/2439

import sys

N = int(sys.stdin.readline())

for i in range(N):
    star = " " * (N - 1 - i) + "*" + "*" * i
    print(star)