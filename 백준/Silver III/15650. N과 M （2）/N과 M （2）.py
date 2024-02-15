import sys
from itertools import combinations
n,m = map(int, sys.stdin.readline().strip().split())
temp = [i for i in range(1,n+1)]
for comb in combinations(temp,m):
    print(*comb)