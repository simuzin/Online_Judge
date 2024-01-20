import sys
n,k = map(int,sys.stdin.readline().strip().split())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]
res = 0
for i in reversed(a):
    if i <= k:
        res += k // i
        k %= i
print(res)