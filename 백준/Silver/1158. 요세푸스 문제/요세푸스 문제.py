from collections import deque
n,k = map(int,input().strip().split())
temp = deque(i for i in range(1,n+1))
key = []
for _ in range(n):
    for _ in range(k-1):
        temp.rotate(-1)
    key.append(temp.popleft())
res = ', '.join(str(i) for i in key).strip()
print(f'<{res}>')