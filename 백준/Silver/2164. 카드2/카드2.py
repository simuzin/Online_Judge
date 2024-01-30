import sys
from collections import deque
n = int(sys.stdin.readline().strip())
card = deque([i for i in range(1,n+1)])
while True:
    if len(card) == 1:
        break
    card.popleft()
    card.rotate(-1)
print(card[0])