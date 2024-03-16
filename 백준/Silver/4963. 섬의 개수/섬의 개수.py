import sys
while True:
    w,h = map(int, sys.stdin.readline().strip().split())
    if w == 0 and h == 0:
        break
    
    if h == 1:
        print(int(input()))
        continue

    ground = []
    for i in range(h):
        ground.append(list(map(int, sys.stdin.readline().strip().split())))

    dirY = [-1,0,1,0,-1,-1,1,1]
    dirX = [0,1,0,-1,-1,1,-1,1]
    queue, isVisit = [], [[False for i in range(w)] for j in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if ground[i][j] == 1 and isVisit[i][j] == False:
                queue.append([i,j])
                isVisit[i][j] = True
                cnt += 1
                while queue:
                    y,x = queue.pop(0)
                    for k in range(8):
                        NextY = dirY[k] + y
                        NextX = dirX[k] + x
                        if (NextY >= 0 and NextY < h and NextX >= 0 and NextX < w) and ground[NextY][NextX] == 1 and isVisit[NextY][NextX] == False:
                            queue.append([NextY,NextX])
                            isVisit[NextY][NextX] = True
    print(cnt)