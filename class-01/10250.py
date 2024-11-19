# https://www.acmicpc.net/problem/10250

import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    q, r = divmod(N, H)

    if r == 0:
        r = H
        q = q - 1

    Y = 100 * r
    XX = q + 1
    YXX = Y + XX
    
    print(YXX)