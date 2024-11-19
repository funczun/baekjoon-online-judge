# https://www.acmicpc.net/problem/3003

import sys

inputs = list(map(int, sys.stdin.readline().split()))

needs = [1, 1, 2, 2, 2, 8]
result = []

for i in range(6):
    result.append(needs[i] - inputs[i])

print(' '.join(map(str, result)))