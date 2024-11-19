# https://www.acmicpc.net/problem/2869

import sys

up, down, height = map(int, sys.stdin.readline().strip().split())
day = 0

if up >= height:
    day = 1
else:
    spend, rest = divmod(height - up, up - down)
    day += spend + 1
    if rest:
        day += 1

print(day)