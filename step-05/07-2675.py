# https://www.acmicpc.net/problem/2675

import sys

T = int(sys.stdin.readline())

for i in range(T):
    result = ""
    R, S = sys.stdin.readline().split()

    for j in S:
        result += int(R) * j

    print(result)