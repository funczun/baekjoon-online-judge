# https://www.acmicpc.net/problem/10811

import sys

N, M = map(int, sys.stdin.readline().split())
baskets = list(range(1, N + 1))

for reverse in range(M):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i - 1:j] = reversed(baskets[i - 1:j])

print(' '.join(map(str, baskets)))