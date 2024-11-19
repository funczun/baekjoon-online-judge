# https://www.acmicpc.net/problem/10810

import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [0] * N

for put in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    baskets[i - 1:j] = [k] * len(baskets[i - 1:j])

result = ' '.join(map(str, baskets))

print(result)