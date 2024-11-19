# https://www.acmicpc.net/problem/2562

import sys

inputs = []

for i in range(9):
    num = int(sys.stdin.readline())
    inputs.append(num)

max_num = max(inputs)

print(max_num)
print(inputs.index(max_num) + 1)