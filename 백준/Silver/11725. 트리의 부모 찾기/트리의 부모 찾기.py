import sys
from collections import deque

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parent_node = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                parent_node[i] = node

bfs(1)
for i in range(2, n+1):
    print(parent_node[i])