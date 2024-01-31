import sys
x = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
temp = 0
for _ in range(n):
    a,b = map(int, sys.stdin.readline().strip().split())
    temp += a*b
print("Yes" if x == temp else "No")