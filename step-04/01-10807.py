# https://www.acmicpc.net/problem/10807

import sys
from collections import Counter

N = int(sys.stdin.readline())
int_list = list(map(int, sys.stdin.readline().split()))

count = Counter(int_list)

v = int(sys.stdin.readline())

print(count[v])