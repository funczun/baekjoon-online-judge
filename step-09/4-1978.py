# https://www.acmicpc.net/problem/1978

import sys

result = 0

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    temp = 0

    for j in range(1, numList[i] + 1):
        if numList[i] % j == 0:
            temp += 1

    if temp == 2:
        result += 1

print(result)