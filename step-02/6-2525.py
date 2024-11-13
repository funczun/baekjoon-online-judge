# https://www.acmicpc.net/problem/2525

import sys

A, B = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

# Add the minutes required to the total time entered.
TM = A * 60 + B + T
A, B = divmod(TM, 60)

# Adjust the hour to be in the range of 0-23
A %= 24

print(f"{A} {B}")