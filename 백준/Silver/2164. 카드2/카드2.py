import sys
from collections import deque

n = int(sys.stdin.readline())
temp = deque([i for i in range(1, n+1)])
while True:
    if len(temp) == 1:
        break
    temp.popleft()
    temp.rotate(-1)
print(temp.pop())
