# https://www.acmicpc.net/problem/9086

import sys

T = int(sys.stdin.readline())

for i in range(T):
    word = sys.stdin.readline().strip()
    print(word[0] + word[len(word) - 1])