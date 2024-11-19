# https://www.acmicpc.net/problem/2745

import sys

num, base = sys.stdin.readline().strip().split()
base = int(base)

result = 0

for i in range(len(num)):
    if num[len(num) - 1 - i].isdigit():
        result += int(num[len(num) - 1 - i]) * pow(base, i)
    else:
        result += (ord(num[len(num) - 1 - i]) - 55) * pow(base, i)

print(result)