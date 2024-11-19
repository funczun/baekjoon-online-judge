# https://www.acmicpc.net/problem/2563

import sys

temp = [0] * 100
arrays = []

for _ in range(100):
    arrays.append(temp.copy())

n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())

    for i in range(10):
        arrays[len(arrays) - (y + i)][x:x + 10] = [1] * 10

total = 0

for array in arrays:
    total += sum(array)

print(total)