import sys

n,m = map(int, sys.stdin.readline().strip().split())
ground = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    s = sys.stdin.readline().strip()
    for j in range(m):
        ground[i][j] = int(s[j])

# 시계 방향으로 순회
dirY = [-1,0,1,0]
dirX = [0,1,0,-1]

# distance이 거리를 저장하는 부분
queue, distance =[], [[-1 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        # 섬의 시작점 찾기
        if ground[i][j] == 1 and distance[i][j] == -1:
            queue.append([i,j])
            distance[i][j] = 1
            # 섬과 이어진 땅 찾기
            while queue:
                y,x = queue.pop(0)
                # 사방으로 찾아보기
                for k in range(4):
                    nextY = y + dirY[k]
                    nextX = x + dirX[k]
                    # 범위를 이탈하지 않고, 한 번도 안 가본 땅 찾기
                    if (nextY < n and nextY >= 0 and nextX < m and nextX >= 0) and (ground[nextY][nextX] == 1) and (distance[nextY][nextX] == -1):
                        queue.append([nextY, nextX])
                        # 거리 계산
                        distance[nextY][nextX] = distance[y][x] +1
print(distance[n-1][m-1])