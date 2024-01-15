import sys
n = int(sys.stdin.readline().strip())
temp = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().strip().split()))
    temp.append(a)
    
res = sorted(temp, key = lambda x:(x[1], x[0]))
for a,b in res:
    print(a,b)