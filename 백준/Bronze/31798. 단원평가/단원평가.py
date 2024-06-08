import sys

a,b,c = map(int, sys.stdin.readline().strip().split())
if a == 0 or b == 0:
    print(c**2 - (b+a))
else:
    print(int((a+b)**(1/2)))