import sys

def find(a):
    if p[a] == a: 
        return a
    else:
        p[a] = find(p[a])
        return p[a]

def union(x,y):
    if r[x] > r[y]:
        p[y] = p[x]
        r[x] += r[y]
    else:
        p[x] = p[y]
        r[y] += r[x]

v,e = map(int, sys.stdin.readline().strip().split())
temp = []
weight, flag = 0, 0
for _ in range(e):
    edge = list(map(int, sys.stdin.readline().strip().split()))
    temp.append(edge)

edges = sorted(temp, key= lambda x:x[2])
p,r = [i for i in range(v+1)], [1]*(v+1)
while edges:
    s,d,w = edges.pop(0)
    DP_s,DP_d = find(s), find(d)
    if DP_s != DP_d:
        union(DP_s,DP_d)
        weight += w
        flag += 1
    if flag == (v-1):
        break
print(weight)