# https://www.acmicpc.net/problem/1546

import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

result = sum(scores) / max(scores) * 100 / N

print(result)