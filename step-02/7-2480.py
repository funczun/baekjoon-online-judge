# https://www.acmicpc.net/problem/2480

import sys
from collections import Counter

d1, d2, d3 = map(int, sys.stdin.readline().split())

# After counting duplicate numbers, put the most frequent value into dup_count.
counts = Counter([d1, d2, d3])
dup_count = max(counts.values())

# Returns the 1 most duplicated element and retrieves the first value of the tuple.
most_dup = counts.most_common(1)[0][0]

if dup_count == 3:
    result = 10000 + most_dup * 1000
elif dup_count == 2:
    result = 1000 + most_dup * 100
else:
    result = max(d1, d2, d3) * 100

print(result)