# https://www.acmicpc.net/problem/1193

import sys

x = int(sys.stdin.readline())

temp = 0
max_in_cycle = 0

while x > max_in_cycle:
    temp += 1
    max_in_cycle += temp

diff = max_in_cycle - x
desc = temp - diff
asc = 1 + diff

if temp % 2 == 0:
    print(f'{desc}/{asc}')
else:
    print(f'{asc}/{desc}')