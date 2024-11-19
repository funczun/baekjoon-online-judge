# https://www.acmicpc.net/problem/2908

import sys

A, B = sys.stdin.readline().split()
rA, rB = A[::-1], B[::-1]

if rA > rB:
    print(rA)
else:
    print(rB)