import sys
from collections import deque

m, n, l = map(int, sys.stdin.readline().split())
board = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(l)]

direction =[(-1, 0, 0),
            (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1),
            (1, 0, 0)]

# bfs
def bfs():

    # 처음에 익은 토마토
    queue = deque([])
    max_day, un_tomato = 0, 0
    for k in range(l):
        for j in range(n):
            for i in range(m):
                if board[k][j][i] == 1:
                    queue.append((k, j, i, 0))
                elif board[k][j][i] == 0:
                    un_tomato += 1
    if not un_tomato:
        print("0")
        return
    
    # 주변 토마토
    while queue:
        h, y, x, day = queue.popleft()
        max_day = max(max_day, day)

        for dir_h, dir_y, dir_x in direction:
            next_y = y + dir_y
            next_x = x + dir_x
            next_h = h + dir_h
            if 0 <= next_h < l and 0 <= next_y < n and 0 <= next_x < m and board[next_h][next_y][next_x] == 0:
                queue.append((next_h, next_y, next_x, day + 1))
                board[next_h][next_y][next_x] = 1
                un_tomato -= 1

    if un_tomato:
        print("-1")
    else:
        print(max_day)

bfs()