import sys

n = int(sys.stdin.readline().strip())
a = set(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))

for i in range(m):
    if b[i] in a:
        print("1")
    else:
        print("0")