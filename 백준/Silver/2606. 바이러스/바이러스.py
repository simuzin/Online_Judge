import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[False] * (n+1) for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

# bfs
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    count = 0

    while queue:
        node = queue.popleft()
        for i in range(1, n+1):
            if graph[node][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                count += 1
    print(count)

bfs(1)