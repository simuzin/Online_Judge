import sys

n = int(sys.stdin.readline().strip())
colors = {'R' : 1, 'G' : 2, 'B' : 3}
location, location_rg = [[0 for i in range(n)] for j in range(n)], [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    temp = sys.stdin.readline().strip()
    for j in range(n):
        location[i][j] = colors[temp[j]]
    for j in range(n):
        temp = temp.replace('R','G')
        location_rg[i][j] = colors[temp[j]]

dirY = [-1,0,1,0]
dirX = [0,1,0,-1]
queue, isVisit = [], [[False for i in range(n)] for j in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if isVisit[i][j] == False:
            color = location[i][j]
            queue.append([i,j])
            isVisit[i][j] = True
            cnt += 1
            while queue:
                y,x = queue.pop(0)
                for k in range(4):
                    NextY = y + dirY[k]
                    NextX = x + dirX[k]
                    if (0<=NextY<n and 0<=NextX<n) and location[NextY][NextX] == color and isVisit[NextY][NextX] == False:
                        queue.append([NextY, NextX])
                        isVisit[NextY][NextX] = True

queue_rg, isVisit_rg = [], [[False for i in range(n)] for j in range(n)]
cnt_rg = 0
for i in range(n):
    for j in range(n):
        if isVisit_rg[i][j] == False:
            color = location_rg[i][j]
            queue_rg.append([i,j])
            isVisit_rg[i][j] = True
            cnt_rg += 1
            while queue_rg:
                y,x = queue_rg.pop(0)
                for k in range(4):
                    NextY = y + dirY[k]
                    NextX = x + dirX[k]
                    if (0<=NextY<n and 0<=NextX<n) and location_rg[NextY][NextX] == color and isVisit_rg[NextY][NextX] == False:
                        queue_rg.append([NextY, NextX])
                        isVisit_rg[NextY][NextX] = True
print(cnt, cnt_rg)