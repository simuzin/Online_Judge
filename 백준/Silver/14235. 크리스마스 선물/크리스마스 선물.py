import heapq
import sys

n = int(sys.stdin.readline().strip())
priority_queue = []

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    if len(nums) == 1:
        if priority_queue:
            present = heapq.heappop(priority_queue)
            print(-present)
        else:
            print("-1")
    else:
        for i in nums[1:]:
            heapq.heappush(priority_queue, -i)