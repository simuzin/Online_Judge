import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().strip().split())
board = [[False for _ in range(n+1)] for _ in range(n+1)]
is_visit_bfs = [False for _ in range(n+1)]
is_visit_dfs = [False for _ in range(n+1)]

for _ in range(m):
    first, second = map(int, sys.stdin.readline().strip().split())
    board[first][second] = board[second][first]= True

# DFS 구현
stack = [v]

while stack:
    num = stack.pop()
    if not is_visit_dfs[num]:
        is_visit_dfs[num] = True
        print(num, end = ' ')

        for i in range(n, 0, -1):
            if board[num][i] and not is_visit_dfs[i]:
                stack.append(i)
            
print('')
# BFS 구현
queue = deque([v])
is_visit_bfs[v] = True
while queue:
    num = queue.popleft()
    print(num, end=' ')

    for i in range(1, n+1):
        if board[num][i] and not is_visit_bfs[i]:
            queue.append(i)
            is_visit_bfs[i] = True