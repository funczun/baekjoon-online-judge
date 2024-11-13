# https://www.acmicpc.net/problem/2577

from collections import Counter

A = int(input())
B = int(input())
C = int(input())

new = str(A * B * C)
counts = Counter(new)

# By setting the default value to 0, prevent the output of None
for i in range(10):
    print(counts.get(str(i), 0))