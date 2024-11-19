# https://www.acmicpc.net/problem/10798

import sys

def index(arrays, index1, index2):
    try:
        return arrays[index1][index2]
    except IndexError:
        return ''

arrays = []

for _ in range(5):
    temp = ' '.join(sys.stdin.readline().strip()).split()
    arrays.append(temp)

result = []

for i in range(15):
    result.append(index(arrays, 0, i))
    result.append(index(arrays, 1, i))
    result.append(index(arrays, 2, i))
    result.append(index(arrays, 3, i))
    result.append(index(arrays, 4, i))

print(''.join(result))