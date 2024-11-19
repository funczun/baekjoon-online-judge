# https://www.acmicpc.net/problem/2438

import sys

N = int(sys.stdin.readline())

for i in range(N):
    star = "*" + "*" * i
    print(star)