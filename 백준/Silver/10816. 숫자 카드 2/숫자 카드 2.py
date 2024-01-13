import sys
from collections import Counter

_ = int(sys.stdin.readline())
key = list(map(int,sys.stdin.readline().split()))
cnt = Counter(key)
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

res = []
for num in nums:
    res.append(cnt[num])
print(' '.join(map(str,res)))