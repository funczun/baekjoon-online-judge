# https://www.acmicpc.net/problem/10950

import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result = A + B
    print(result)