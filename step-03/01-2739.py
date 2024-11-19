# https://www.acmicpc.net/problem/2739

N = int(input())
M = list(range(1, 10))

for i in M:
    r = N * i
    print(f"{N} * {i} = {r}")