import sys
from itertools import permutations
n,m = map(int, sys.stdin.readline().strip().split())
temp = [i for i in range(1,n+1)]
for permu in permutations(temp,m):
    print(*permu)