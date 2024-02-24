import sys
from collections import Counter
n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()
print(round(sum(nums)/n))
print(nums[(n//2)])
if n == 1:
    print(nums[0])
else:
    temp = Counter(nums).most_common(2)
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
print(nums[-1]-nums[0])