import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().strip().split())
graph = [[False for _ in range(n+1)] for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = True

# DFS 구현 (재귀 없이 스택 사용)
def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited_dfs[node]:
            visited_dfs[node] = True
            print(node, end = ' ')

            # 작은 번호부터 방문하기 위해, 역순
            for i in range(n, 0, -1):
                if graph[node][i] and not visited_dfs[i]:
                    stack.append(i)

# BFS 구현 (큐 사용)
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in range(1, n+1):
            if graph[node][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)