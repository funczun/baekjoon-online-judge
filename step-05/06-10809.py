# https://www.acmicpc.net/problem/10809

import sys

S = sys.stdin.readline().strip()
result = []

# The find method returns -1 when the substring being searched for is not found
for i in range(ord('a'), ord('z') + 1):
    temp = S.find(chr(i))
    result.append(str(temp))

print(' '.join(result))