import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited_bfs = [False for _ in range(100001)]
after = ['-1', '+1', '*2']

def bfs(n, k):
    queue = deque([(n, 0)])
    visited_bfs[n] = True

    while queue:
        num, cnt = queue.popleft()

        if num == k:
            print(cnt)
            return

        for operation in after:
            after_min = eval(f'{num} {operation}')
            if after_min >= 0 and after_min <=100000 and not visited_bfs[after_min]:
                queue.append((after_min, cnt+1))
                visited_bfs[after_min] = True

bfs(n, k)