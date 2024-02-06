import sys
from collections import Counter
n = int(sys.stdin.readline().strip())
res = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 2 and (stack[-2] == stack[-1]):
            stack.pop()
    a,b = Counter(stack).most_common(1)[0]
    if b == 1:
        res += 1
print(res)