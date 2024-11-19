# https://www.acmicpc.net/problem/2920

import sys

num = sys.stdin.readline().strip()

if list(''.join(num.split())) == sorted(''.join(num.split())):
    print("ascending")
elif list(''.join(num.split())) == sorted(''.join(num.split()))[::-1]:
    print("descending")
else:
    print("mixed")