# https://www.acmicpc.net/problem/2884

import sys

# Convert the entered hours and minutes into total minutes.
H, M = map(int, sys.stdin.readline().split())
TM = H * 60 + M - 45

# Handle negative total minutes.
if TM < 0:
    TM += 1440

# Adjust the hour to be in the range of 0-23.
H, M = divmod(TM, 60)
H %= 24

print(f"{H} {M}")