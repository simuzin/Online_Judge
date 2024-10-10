import sys
from collections import deque

t = int(sys.stdin.readline().strip())
for _ in range(t):
    l = int(sys.stdin.readline().strip())
    is_visit = [[0] * l for __ in range(l)]

    # BFS 구현
    start_x, start_y = map(int, sys.stdin.readline().strip().split())
    end_x, end_y = map(int, sys.stdin.readline().strip().split())
    is_visit[start_y][start_x] = True

    queue = deque([(start_y, start_x, 0)])
    dir = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

    while queue:
        y,x,cnt = queue.popleft()

        if x == end_x and y == end_y:
            print(cnt)
            break

        for dir_x, dir_y in dir:
            next_y = y + dir_y
            next_x = x + dir_x

            if next_y >= 0 and next_x >= 0 and next_y < l and next_x < l and not is_visit[next_y][next_x]:
                is_visit[next_y][next_x] = True
                queue.append((next_y, next_x, cnt+1))