import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dir_y, dir_x = [1,0,-1,0],[0,1,0,-1]
power = [0,0]
def bfs(j, i, c):
    queue = deque([(j,i)])
    cnt = 1
    while queue:
        y,x = queue.popleft()
        for k in range(4):
            next_y = y + dir_y[k]
            next_x = x + dir_x[k]

            if 0<=next_y<N and 0<=next_x<M and board[next_y][next_x] == c and not visited[next_y][next_x]:
                cnt += 1
                visited[next_y][next_x] = True
                queue.append((next_y,next_x))
    return cnt**2

for j in range(N):
    for i in range(M):
        if board[j][i] and not visited[j][i]:
            c = board[j][i]
            visited[j][i] = True
            if c == 'W':
                power[0] += bfs(j,i,c)
            else:
                power[1] += bfs(j,i,c)

print(*power)