import sys
n = int(sys.stdin.readline().strip())
name = [sys.stdin.readline().strip() for _ in range(n)] 
temp = sorted(name)
if name == temp:
    print("INCREASING")
elif name == temp[::-1]:
    print("DECREASING")
else:
    print("NEITHER")