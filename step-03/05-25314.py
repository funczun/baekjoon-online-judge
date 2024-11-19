# https://www.acmicpc.net/problem/25314

import sys

N = int(sys.stdin.readline())

result = ""

for i in range(N // 4):
    result += "long "

result += "int"

print(result)