# https://www.acmicpc.net/problem/2738

import sys

n, m = map(int, sys.stdin.readline().split())

first_array = []
second_array = []

for _ in range(n):
    row = list(sys.stdin.readline().strip().split())
    first_array.append(row)

for _ in range(n):
    row = list(sys.stdin.readline().strip().split())
    second_array.append(row)

new_array = []

for i in range(n):
    new_row = []

    for f, s in zip(first_array[i], second_array[i]):
        new_row.append(int(f) + int(s))
    new_array.append(new_row)

for new_row in new_array:
    print(' '.join(map(str, new_row)))