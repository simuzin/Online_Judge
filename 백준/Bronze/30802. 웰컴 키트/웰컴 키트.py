import sys

n = int(sys.stdin.readline().strip())
size = list(map(int,sys.stdin.readline().strip().split()))
t,p = map(int, sys.stdin.readline().strip().split())

result = 0
for i in size:
    result += (i // t)
    if i % t > 0:
        result += 1
print(result)
print(n//p, n%p)