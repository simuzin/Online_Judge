import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited_bfs = [[False] * m for _ in range(n)]
board_cnt = [[-1] * m for _ in range(n)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def find_goal():
    goal_y, goal_x = 0, 0
    for j in range(n):
        for i in range(m):
            if board[j][i] == 2:
                board_cnt[j][i] = 0
                goal_y, goal_x = j, i
            elif board[j][i] == 0:
                board_cnt[j][i] = 0
    return goal_y, goal_x

def bfs(goal_y, goal_x):
        queue = deque([(goal_y, goal_x, 0)])
        visited_bfs[goal_y][goal_x] = True

        while queue:
            y, x, cnt = queue.popleft()
            for dir_y, dir_x in direction:
                next_y = y + dir_y
                next_x = x + dir_x
                if 0 <= next_y < n and 0 <= next_x < m and board[next_y][next_x] == 1 and not visited_bfs[next_y][next_x]:
                    queue.append((next_y, next_x, cnt+1))
                    visited_bfs[next_y][next_x] = True
                    board_cnt[next_y][next_x] = cnt+1
        for j in range(n):
            print(*board_cnt[j])

goal_y, goal_x = find_goal()
bfs(goal_y, goal_x)