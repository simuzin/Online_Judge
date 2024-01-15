import sys
from itertools import combinations

_,m = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
data = {}
for comb in combinations(temp,3):
    if sum(comb) <= m:
        data[abs(m-sum(comb))] = sum(comb)
res = sorted(data.items(), key = lambda x:x[0])
print(res[0][1])