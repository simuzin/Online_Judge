import sys
from collections import deque
n= int(sys.stdin.readline().strip())
queue = deque([])
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if queue:
            print("0")
        else:
            print("1")
    elif s == 'front':
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif s == 'back':
        if queue:
            print(queue[-1])
        else:
            print("-1")
    else:
        _, i = s.split()
        queue.append(i)