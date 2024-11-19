# https://www.acmicpc.net/problem/2292

import sys

n = int(sys.stdin.readline())

mini, maxi = 1, 1
room_count = 1

while n > maxi:
        mini = maxi + 1
        maxi += 6 * room_count
        room_count += 1

print(room_count)