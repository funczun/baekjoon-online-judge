# https://www.acmicpc.net/problem/10988

import sys

inputs = sys.stdin.readline().strip()

if inputs[::-1] == inputs:
    print(1)
else:
    print(0)