# https://www.acmicpc.net/problem/1157

import sys
from collections import Counter

inputWord = sys.stdin.readline().strip().upper()
countDict = Counter(inputWord)

mostCommon = countDict.most_common(2)
a, b = mostCommon[0]

if len(mostCommon) > 1:
    c, d = mostCommon[1]

    if b == d:
        print('?')
        sys.exit()

print(a)