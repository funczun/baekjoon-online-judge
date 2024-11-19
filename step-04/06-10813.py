# https://www.acmicpc.net/problem/10813

import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [num for num in range(1, N + 1)]

for swap in range(M):
    i, j = map(int, sys.stdin.readline().split())
    s = baskets[i - 1]
    baskets[i - 1] = baskets[j - 1]
    baskets[j - 1] = s

print(' '.join(map(str, baskets)))