import sys

input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dir_y, dir_x = [1,0,-1,0],[0,1,0,-1]
result = []
cnt = 0

def dfs(j,i):
    global cnt
    cnt += 1
    for k in range(4):
        y = j + dir_y[k]
        x = i + dir_x[k]
        if 0<=y<N and 0<=x<N and board[y][x]==1 and not visited[y][x]:
            visited[y][x] = True
            dfs(y,x)


for j in range(N):
    for i in range(N):
        if board[j][i]==1 and not visited[j][i]:
            visited[j][i] = True
            cnt = 0
            dfs(j,i)
            result.append(cnt)

result.sort()
print(len(result))
for res in result:
    print(res)