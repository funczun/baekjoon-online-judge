# https://www.acmicpc.net/problem/2720

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c = int(sys.stdin.readline())
    quarter, c = divmod(c, 25)
    dime, c = divmod(c, 10)
    nickel, penny = divmod(c, 5)
    print(quarter, dime, nickel, penny)