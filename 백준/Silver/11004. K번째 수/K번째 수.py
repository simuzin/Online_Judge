import sys
_,k = map(int,sys.stdin.readline().strip().split())
temp = list(map(int, sys.stdin.readline().strip().split()))
temp.sort()
print(temp[k-1])