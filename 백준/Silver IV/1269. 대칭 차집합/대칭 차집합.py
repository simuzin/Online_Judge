import sys
_,__= map(int,sys.stdin.readline().strip().split())
a = set(list(map(int,sys.stdin.readline().strip().split())))
b = set(list(map(int,sys.stdin.readline().strip().split())))
print(len(a-b)+len(b-a))