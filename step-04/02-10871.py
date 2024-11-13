# https://www.acmicpc.net/problem/10871

import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
less_than = []

for i in A:
    if i < X:
        less_than.append(i)

# To convert each element to a string, you should use the map function
result = map(str, less_than)

print(' '.join(result))