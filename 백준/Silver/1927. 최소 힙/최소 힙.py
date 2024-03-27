import sys
import heapq

n = int(sys.stdin.readline().strip())
priority_queue = []

for i in range(n):
    key = int(sys.stdin.readline().strip())
    if key == 0:
        if len(priority_queue) == 0:
            print("0")
        else:
            temp = heapq.heappop(priority_queue)
            print(temp)
    else:
        heapq.heappush(priority_queue, key)