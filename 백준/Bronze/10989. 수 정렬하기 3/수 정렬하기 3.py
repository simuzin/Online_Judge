import sys

n = int(sys.stdin.readline().strip())
temp = [0] * 10001
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    temp[a] += 1

for i in range(len(temp)):
    if temp[i] != 0:
        for j in range(temp[i]):
            print(i)