import sys
n,m = map(int, sys.stdin.readline().strip().split())
s, count = [], 0
for _ in range(n):
    s.append(sys.stdin.readline().strip())
for _ in range(m):
   temp = sys.stdin.readline().strip()
   if temp in s:
       count+=1
print(count) 