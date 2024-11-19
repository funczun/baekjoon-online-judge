# https://www.acmicpc.net/problem/25304

import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

total_price = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    price = a * b
    total_price += price

if X == total_price:
    print("Yes")
else:
    print("No")