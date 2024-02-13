import sys
from itertools import permutations
n = sys.stdin.readline().strip()
temp = [int(i) for i in n]

if (sum(temp) % 3 == 0) and (0 in temp):
    print(''.join(sorted(n, reverse=True)))
else:
    print("-1")
