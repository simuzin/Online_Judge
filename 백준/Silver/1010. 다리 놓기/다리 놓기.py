import sys
import math
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().strip().split())
    print(math.comb(m,n))