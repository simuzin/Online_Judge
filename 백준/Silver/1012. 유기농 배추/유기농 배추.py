import sys

t = int(sys.stdin.readline().strip())

dirY = [-1,0,1,0]
dirX = [0,1,0,-1]

for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().strip().split())
    ground = [[0 for j in range(m)] for i in range(n)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().strip().split())
        ground[y][x] = 1
    # print(ground)
    queue, isVisit = [], [[False for j in range(m)] for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            # 현재 값이 1이면서 방문 안 했을 경우,
            if (ground[i][j] == 1) and (isVisit[i][j] == False):
                cnt += 1
                isVisit[i][j] = True
                queue.append([i,j])
                # 섬 만들기
                while len(queue) > 0:
                    temp = queue.pop(0)
                    # 이어진 땅 찾기
                    for k in range(4):
                        nextY = temp[0]+dirY[k]
                        nextX = temp[1]+dirX[k]
                        if (nextY >= 0 and nextY < n and nextX >=0 and nextX < m)and (ground[nextY][nextX] == 1) and (isVisit[nextY][nextX] == False):
                                queue.append([nextY,nextX])
                                isVisit[nextY][nextX] = True
    print(cnt)