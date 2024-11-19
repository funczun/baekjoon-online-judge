# https://www.acmicpc.net/problem/5622

import sys

def match(a):
    if ord(a) < 68:
        return 3
    elif ord(a) < 71:
        return 4
    elif ord(a) < 74:
        return 5
    elif ord(a) < 77:
        return 6
    elif ord(a) < 80:
        return 7
    elif ord(a) < 84:
        return 8
    elif ord(a) < 87:
        return 9
    else:
        return 10

gmNum = sys.stdin.readline().strip()

time = 0

for i in gmNum:
    time += match(i)

print(time)