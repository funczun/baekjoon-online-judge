# https://www.acmicpc.net/problem/2501

import sys

n, k = map(int, sys.stdin.readline().split())

factors = []

for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)

    if len(factors) == k:
        print(factors.pop())
        exit()

print(0)