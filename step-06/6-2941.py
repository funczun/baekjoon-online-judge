# https://www.acmicpc.net/problem/2941

import sys

userInput = sys.stdin.readline().strip()

alphabetList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for letter in alphabetList:
    userInput = userInput.replace(letter, '?')

print(len(userInput))