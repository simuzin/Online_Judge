import sys

a,b,c = map(int, sys.stdin.readline().strip().split())
print(a+c if a+c >= b else b)