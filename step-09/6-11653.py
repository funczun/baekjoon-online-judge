# https://www.acmicpc.net/problem/11653

import sys

n = int(sys.stdin.readline())

while n != 1:
    for i in range(2, n + 1):

        if n % i == 0:
            n = n // i
            print(i)
            break