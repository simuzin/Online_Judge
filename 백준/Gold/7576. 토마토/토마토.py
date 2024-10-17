from collections import deque
import sys

# 입력
m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dir_y, dir_x = [0, 1, 0, -1], [1, 0, -1, 0]

# BFS 구현
def bfs():
    # 초기에 익은 토마토
    queue = deque([])
    for j in range(n):
        for i in range(m):
            if board[j][i] == 1:
                queue.append((j, i, 0))

    max_day = -1

    # 토마토 익히기
    while queue:
        y, x, day = queue.popleft()
        max_day = max(max_day, day)
        for i in range(4):
            next_y = y + dir_y[i]
            next_x = x + dir_x[i]
            if 0 <= next_y < n and 0 <= next_x < m and board[next_y][next_x] == 0:
                queue.append((next_y, next_x, day+1))
                board[next_y][next_x] = 1

    flat_board = sum(board,[])
    if 0 in flat_board:
        print("-1")
    else:
        print(max_day)

bfs()