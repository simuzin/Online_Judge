import sys

n,m = map(int, sys.stdin.readline().strip().split())
a = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    a.append(temp)  

for i in range(n) : 
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        a[i][j] += temp[j]
    print(*a[i])