def solution(maps):
    n,m = len(maps), len(maps[0])
    
    dirY = [-1,0,1,0]
    dirX = [0,1,0,-1]
    queue, distance =[[0,0]], [[-1 for i in range(m)] for j in range(n)]
    distance[0][0] = True
    
    while queue:
        y,x = queue.pop(0)
        for k in range(4):
            NextY = y + dirY[k]
            NextX = x + dirX[k]
            if (NextY >= 0 and NextY < n and NextX >= 0 and NextX < m) and maps[NextY][NextX] == 1 and distance[NextY][NextX] == -1:
                queue.append([NextY,NextX])
                distance[NextY][NextX] = distance[y][x] + 1
    return distance[n-1][m-1]