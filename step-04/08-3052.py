# https://www.acmicpc.net/problem/3052

import sys

rest = set()

for i in range(10):
    n = int(sys.stdin.readline())
    rest.add(n % 42)

print(len(rest))