# https://www.acmicpc.net/problem/1316

import sys

n = int(sys.stdin.readline().strip())

group = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    last = ''
    temp = []
    check = True

    for letter in word:
        if letter != last:
            if letter in temp:
                check = False
            temp.append(letter)
            last = letter

    if check == True:
        group += 1

print(group)