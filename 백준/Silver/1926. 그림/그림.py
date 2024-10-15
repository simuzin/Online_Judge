import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited_bfs = [[False] * m for _ in range(n)]

# bfs
def bfs():
    queue = deque([])
    dir_y, dir_x = [1, 0, -1, 0], [0, 1, 0, -1]
    drawing_cnt, max_drawing = 0, 0
    for j in range(n):
        for i in range(m):
            if board[j][i] and not visited_bfs[j][i]:
                queue.append((j, i))
                visited_bfs[j][i] = True
                drawing_cnt += 1
                cnt = 1
                while queue:
                    y, x = queue.popleft()
                    for i in range(4):
                        next_y = y + dir_y[i]
                        next_x = x + dir_x[i]
                        if next_y >= 0 and next_x >= 0 and next_y < n and next_x < m and board[next_y][next_x] and not visited_bfs[next_y][next_x]:
                            queue.append((next_y, next_x))
                            visited_bfs[next_y][next_x] = True
                            cnt += 1
                max_drawing = max(max_drawing, cnt)
    print(drawing_cnt)
    print(max_drawing)

bfs()