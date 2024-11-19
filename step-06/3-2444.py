# https://www.acmicpc.net/problem/2444

import sys

N = int(sys.stdin.readline())
l = N * 2 - 1

for i in range(l):
    if i < N - 1:
        print(' ' * (N - 1 - i) + '*' * (1 + 2 * i))
    elif i == N - 1:
        print('*' * l)
    else:
        print(' ' * (i - (N - 1)) + '*' * (l - 2 - 2 * (i - N)))