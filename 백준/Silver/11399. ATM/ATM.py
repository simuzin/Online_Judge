import sys
n = int(sys.stdin.readline().strip())
p = list(map(int,sys.stdin.readline().strip().split()))
p.sort()

res = 0
for i in range(n):
    res += sum(p[:i+1])
print(res)