# https://www.acmicpc.net/problem/10950

import sys

# Enter the number of calculation trials
T = int(sys.stdin.readline())

# Repeat calculation until T value becomes 0 and becomes False.
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result = A + B
    print(result)