from collections import deque
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    for j in range(n):
        for i in range(m):
            if maps[j][i] == 'S':
                start_y, start_x = j, i
            elif maps[j][i] =='L':
                lever_y, lever_x = j, i
            elif maps[j][i] =='E':
                end_y, end_x = j, i
    visited = [[False] * m for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # BFS
    def BFS (_y, _x, type):
        visited = [[False] * m for _ in range(n)]
        visited[_y][_x] = True
        queue = deque([(_y, _x, 0)])
        if type == 'lever':
            finish_y, finish_x = lever_y, lever_x
        else:
            finish_y, finish_x = end_y, end_x

        while queue:
            y, x, day = queue.popleft()
            if y == finish_y and x == finish_x:
                return day

            for dir_y, dir_x in directions:
                next_y = y + dir_y
                next_x = x + dir_x

                if 0 <= next_y < n and 0 <= next_x < m and maps[next_y][next_x] != 'X' and not visited[next_y][next_x]:
                    queue.append((next_y, next_x, day + 1))
                    visited[next_y][next_x] = True
        return -1
    for y, x, target in [(start_y, start_x, 'lever'), (lever_y, lever_x, 'end')]:
        temp = BFS(y, x, target)
        if temp > 0:
            answer += temp
        else:
            return -1
    return answer