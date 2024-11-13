# https://www.acmicpc.net/problem/10810

import sys

# Since each basket can hold only one value, create a single list of baskets
N, M = map(int, sys.stdin.readline().split())
baskets = [0] * N

# Be careful with indexing
for put in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    baskets[i - 1:j] = [k] * len(baskets[i - 1:j])

# The join function raises an error when it encounters a value that is not a str
result = ' '.join(map(str, baskets))

print(result)