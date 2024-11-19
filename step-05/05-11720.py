# https://www.acmicpc.net/problem/11720

import sys

N = int(sys.stdin.readline().strip())
numList = list(sys.stdin.readline().strip())
numList_int = map(int, numList)

print(sum(numList_int))