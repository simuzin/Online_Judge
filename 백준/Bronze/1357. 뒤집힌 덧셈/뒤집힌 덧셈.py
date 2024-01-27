import sys
x,y = sys.stdin.readline().strip().split()
x = int(x[::-1])
y = int(y[::-1])
n = str(x+y)
print(int(n[::-1]))