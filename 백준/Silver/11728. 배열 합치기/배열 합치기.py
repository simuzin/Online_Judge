import sys
_,__ = map(int,sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
a.extend(b)
a.sort()
print(*a)
