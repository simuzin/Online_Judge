import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[False] * (n+1) for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

# 그래프 만들기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = True

# bfs 구현
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        node = queue.popleft()
        for i in range(1, n+1):
            if graph[node][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

count = 0
for i in range(1, n+1):
    if not visited_bfs[i]:
        bfs(i)
        count += 1
print(count)