import sys

n = int(sys.stdin.readline().strip())
ground = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    s = sys.stdin.readline().strip()
    for j in range(n):
        ground[i][j] = int(s[j])

# 시계 방향으로 순회 (상, 우, 하, 좌)
dirY = [-1,0,1,0]
dirX = [0,1,0,-1]
queue, home =[], [[0 for i in range(n)] for j in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if ground[i][j] == 1 and home[i][j] == 0:
            queue.append([i,j])
            cnt += 1
            home[i][j] = cnt
            while queue:
                y,x = queue.pop(0)
                for k in range(4):
                    nextY = y + dirY[k]
                    nextX = x + dirX[k]
                    if (nextY < n and nextY >= 0 and nextX < n and nextX >= 0) and (ground[nextY][nextX] == 1) and (home[nextY][nextX] == 0):
                        queue.append([nextY, nextX])
                        home[nextY][nextX] = cnt

# 출력
print(cnt)
res = [0 for i in range(cnt+1)]
for k in range(n):
    for i in range(1,cnt+1):
        res[i] += home[k].count(i)
res.sort()
for i in range(1, cnt+1):
    print(res[i])