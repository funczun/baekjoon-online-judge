# https://www.acmicpc.net/problem/5597

import sys

check = [num for num in range(1, 31)]

for i in range(28):
    n = int(sys.stdin.readline())
    check.remove(n)

print(check[0])
print(check[1])