import sys

def find(a):
    if p[a] == a: return a
    else:
        p[a] = find(p[a])
        return p[a]

def union(x,y):
    x_root = find(x)
    y_root = find(y)
    if r[x_root] > r[y_root]:
        p[y_root] = x_root
    elif r[x_root] < r[y_root]:
        p[x_root] = y_root
    else:
        p[y_root] = x_root
        r[x_root] += 1

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

_edges = []
for _ in range(m): 
    edge = list(map(int, sys.stdin.readline().strip().split()))
    _edges.append(edge)

edges = sorted(_edges, key = lambda x:x[2])
p, r = [i for i in range(n+1)], [1]*(n+1)
answer, flag = 0,0
while edges:
    s,d,w = edges.pop(0)
    if find(s) != find(d):
        union(s,d)
        answer += w
        flag += 1

    if flag == (n-1):
        break
print(answer)