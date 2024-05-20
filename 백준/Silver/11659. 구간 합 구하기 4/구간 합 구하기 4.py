import sys
n,m = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

sum = [0] * (n+1)
for i in range(1,n+1):
    sum[i] = sum[i-1] + num_list[i-1]

for _ in range(m):
    s,e = map(int, sys.stdin.readline().strip().split())
    print(sum[e] - sum[s-1])