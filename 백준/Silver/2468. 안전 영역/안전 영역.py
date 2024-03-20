import sys

n = int(sys.stdin.readline().strip())
height, location = [], []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    location.append(temp)
    height.extend(set(temp))
height = sorted(list(set(height)))

dirY = [-1,0,1,0]
dirX = [0,1,0,-1]
res =[]
for h in height:
    maps, cnt = [], 0
    queue, isVisit = [], [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        maps.append([])
        for j in range(n):
            if location[i][j] <= h:
                maps[-1].append(0)
            else:
                maps[-1].append(1)
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1 and isVisit[i][j] == False:
                queue.append([i,j])
                isVisit[i][j] = True
                cnt += 1
                while queue:
                    y,x = queue.pop(0)
                    for k in range(4):
                        NextY = y + dirY[k]
                        NextX = x + dirX[k]
                        if (0<=NextY<n and 0<=NextX<n) and maps[NextY][NextX] == 1 and isVisit[NextY][NextX] == False:
                            queue.append([NextY, NextX])
                            isVisit[NextY][NextX] = True
                res.append(cnt)
if res:
    print(max(res))
else:
    print(1)