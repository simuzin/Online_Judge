import sys
from collections import deque

input = sys.stdin.readline
M, N, K = map(int, input().split())

board = [[1] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
dir_y, dir_x = [1,0,-1,0],[0,1,0,-1]
result = []
cnt = 0

for _ in range(K):
    first_x, first_y, second_x, second_y = map(int, input().split())
    for j in range(first_y, second_y):
        for i in range(first_x, second_x):
            board[j][i] = 0

def dfs(y,x):
    global cnt
    cnt += 1

    for k in range(4):
        next_y = y + dir_y[k]
        next_x = x + dir_x[k]
        if 0<=next_y<M and 0<=next_x<N and board[next_y][next_x] == 1 and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            dfs(next_y,next_x)


def bfs(y,x):
    queue = deque([(y,x)])
    count = 1
    while queue:
        curr_y,curr_x = queue.popleft()
        for k in range(4):
            next_y = curr_y + dir_y[k]
            next_x = curr_x + dir_x[k]
            if 0<=next_y<M and 0<=next_x<N and board[next_y][next_x] == 1 and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                queue.append((next_y,next_x))
                count += 1
    return count

for j in range(M):
    for i in range(N):
        if board[j][i] == 1 and not visited[j][i]:
            visited[j][i] = True
            # cnt = 0
            # dfs(j,i)
            # result.append(cnt)

            result.append(bfs(j,i))
            cnt += 1

result.sort()
print(len(result))
print(*result)