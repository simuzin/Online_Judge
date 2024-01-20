import sys
n = int(sys.stdin.readline().strip())
temp = []
for _ in range(n):
    temp.append(int(sys.stdin.readline().strip()))
temp.sort()
for i in range(n):
    print(temp[i])