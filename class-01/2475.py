# https://www.acmicpc.net/problem/2475

import sys

def mul(x):
    return x * x

a, b, c, d, e = map(int, sys.stdin.readline().split())
numMul = map(mul, [a, b, c, d, e])
result = sum(numMul) % 10

print(result)