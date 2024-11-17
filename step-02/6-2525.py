# https://www.acmicpc.net/problem/2525

import sys

A, B = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

TM = A * 60 + B + T
A, B = divmod(TM, 60)
A %= 24

print(f"{A} {B}")