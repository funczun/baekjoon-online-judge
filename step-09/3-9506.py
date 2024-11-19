# https://www.acmicpc.net/problem/9506

import sys

while True:
    factors = set()
    n = int(sys.stdin.readline())

    if n == -1:
        break

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    factors = sorted(factors)
    factors.pop()

    if sum(factors) == n:
        print(f"{n} = {' + '.join(map(str, factors))}")
    else:
        print(f"{n} is NOT perfect.")