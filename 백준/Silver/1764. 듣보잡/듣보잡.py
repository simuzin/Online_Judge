import sys
n,m = map(int,sys.stdin.readline().strip().split())
temp,res = {},[]
for _ in range(n+m):
    s = sys.stdin.readline().strip()
    if s not in temp:
        temp[s] = 1
    else:
        temp[s] += 1
        res.append(s)
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])