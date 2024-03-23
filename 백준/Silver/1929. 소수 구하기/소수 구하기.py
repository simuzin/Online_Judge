import sys
m,n = map(int, sys.stdin.readline().strip().split())

temp = [False, False] + [True]*(n+1)
for i in range(2, n+1):
    if temp[i] and i >= m:
        print(i)
    for j in range(2*i,n+1,i):
        temp[j] = False