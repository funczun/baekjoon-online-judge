# https://www.acmicpc.net/problem/2581

import sys

numList = []

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

for i in range(m, n + 1):
    temp = 0

    for j in range(1, n + 1):
        if i % j == 0:
            temp += 1

    if temp == 2:
        numList.append(i)

if len(numList) == 0:
    print(-1)
else:
    print(sum(numList))
    print(min(numList))