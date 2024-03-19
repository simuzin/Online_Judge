def solution(land):
    n, m = len(land), len(land[0])

    dirY = [-1, 0, 1, 0]
    dirX = [0, 1, 0, -1]
    queue, location = [], [[-1 for i in range(m)] for j in range(n)]
    num, key  = 1, {}
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and location[i][j] == -1:
                queue.append([i,j])
                location[i][j] = num
                count = 1
                while queue:
                    y,x = queue.pop(0)
                    for k in range(4):
                        NextY = y + dirY[k]
                        NextX = x + dirX[k]
                        if (0<=NextY<n and 0<=NextX<m) and land[NextY][NextX] == 1 and location[NextY][NextX] == -1:
                            queue.append([NextY, NextX])
                            location[NextY][NextX] = num
                            count += 1
                key[num] = count
                num += 1
    
    res = []
    for x in range(m):
        temp, cnt = [], 0
        for y in range(n):
            if location[y][x] > 0:
                temp.append(location[y][x])
        for k in set(temp):
            cnt += key[k]
        res.append(cnt)
    return max(res)