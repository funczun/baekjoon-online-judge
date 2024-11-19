# https://www.acmicpc.net/problem/2903

import sys

n = int(sys.stdin.readline())

temp = 0

for i in range(n):
    temp += pow(2, i)

print(pow(2 + temp, 2))