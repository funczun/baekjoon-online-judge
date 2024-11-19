# https://www.acmicpc.net/problem/25206

import sys

convDict = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
    }

grade_list = []
total_credit = 0

for _ in range(20):
    inf = list(sys.stdin.readline().strip().split())
    credit = float(inf[1])
    grade = inf[2]

    if grade != 'P':
        grade_list.append(convDict[grade] * credit)
        total_credit += credit

print(sum(grade_list) / total_credit)