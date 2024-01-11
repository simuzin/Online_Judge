import sys
from collections import Counter
n,m = map(int,sys.stdin.readline().strip().split())
temp = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    if len(s) >= m:
        temp.append(s)
answer = Counter(temp)
answer = sorted(answer.items(), key = lambda x: (-x[1],-len(x[0]),x[0]))
for res, _ in answer:
    print(res)
