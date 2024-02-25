import sys

def find(a):
    if p[a] == a: return a
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

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

_edges = []
for _ in range(m): 
    edge = list(map(int, sys.stdin.readline().strip().split()))
    _edges.append(edge)

edges = sorted(_edges, key = lambda x:x[2])
p, r = [i for i in range(n+2)], [1]*(n+1)
answer, flag = 0,0
while edges:
    s,d,w = edges.pop(0)
    x = find(s)
    y = find(d)
    if x != y:
        union(x,y)
        answer += w
        flag += 1

    if flag == n-1:
        break
print(answer)