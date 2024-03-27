import heapq
import sys

n = int(sys.stdin.readline().strip())
priority_queue = []

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    if not priority_queue:
        for num in nums:
            heapq.heappush(priority_queue, num)
    else:
        for num in nums:
            if priority_queue[0] < num:
                heapq.heappush(priority_queue,num)
                heapq.heappop(priority_queue)
print(priority_queue[0])