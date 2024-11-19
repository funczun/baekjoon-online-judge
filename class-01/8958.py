# https://www.acmicpc.net/problem/8958

import sys

attempts = int(sys.stdin.readline())

for i in range(attempts):
    stack = 0
    stackList = []
    inputs = sys.stdin.readline().strip()

    for _ in range(len(inputs)):
        if inputs[_] == 'O':
            stack += 1
            stackList.append(stack)
        else:
            stack = 0

    print(sum(stackList))