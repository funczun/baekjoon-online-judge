# https://www.acmicpc.net/problem/25314

import sys

N = int(sys.stdin.readline())

# Set the initial value to "" to add strings
result = ""

# Add a string for every multiple of 4
for i in range(N // 4):
    result += "long "

result += "int"

print(result)