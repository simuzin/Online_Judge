import sys
from collections import deque

n = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

flat_board = sum(board,[])
min_height, max_height = min(flat_board), max(flat_board),

def bfs(water):
    visited_bfs = [[False] * n for _ in range(n)]

    queue = deque([])
    dir_y, dir_x = [1, 0, -1, 0], [0, 1, 0, -1]
    cnt = 0
    for j in range(n):
        for i in range(n):
            if board[j][i] > water and not visited_bfs[j][i]:
                queue.append((j, i))
                visited_bfs[j][i] = True
                cnt += 1
                while queue:
                    y, x = queue.popleft()
                    for i in range(4):
                        next_y = y + dir_y[i]
                        next_x = x + dir_x[i]
                        if next_y >= 0 and next_x >= 0 and next_y < n and next_x<n and board[next_y][next_x] > water and not visited_bfs[next_y][next_x]:
                            queue.append((next_y, next_x))
                            visited_bfs[next_y][next_x] = True
    return cnt

max_cnt = 1
for i in range(min_height, max_height):
    max_cnt = max(max_cnt, bfs(i))
print(max_cnt)