# https://www.acmicpc.net/problem/11005

import sys

num, base = map(int, sys.stdin.readline().strip().split())

rList = []
cList = []

while num > 0:
    num, r = divmod(num, base)
    rList.append(r)

for rest in rList:
    if rest >= 10:
        cList.append(chr(rest + 55))
    else:
        cList.append(rest)

cList.reverse()
result = ''.join(map(str, cList))

print(result)