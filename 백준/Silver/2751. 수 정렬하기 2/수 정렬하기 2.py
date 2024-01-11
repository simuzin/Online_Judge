import sys
n = int(sys.stdin.readline())
temp = []
for _ in range(n):
    temp.append(int(sys.stdin.readline()))
temp.sort()
for i in range(n):
    print(temp[i])