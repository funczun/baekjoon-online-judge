# https://www.acmicpc.net/problem/10869

import sys

# Use stdin.readline() to read a line from standard input.
A, B = map(int, sys.stdin.readline().split())

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)