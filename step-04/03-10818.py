# https://www.acmicpc.net/problem/10818

import sys

N = int(sys.stdin.readline())
int_list = list(map(int, sys.stdin.readline().split()))

print(f"{min(int_list)} {max(int_list)}")