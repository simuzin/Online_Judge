import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
a.sort()
b.sort(reverse = True)

s = 0
for i in range(n):
    s += a[i] * b[i]
print(s)