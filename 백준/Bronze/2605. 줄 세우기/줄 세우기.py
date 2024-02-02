import sys
n = int(sys.stdin.readline().strip())
temp = list(map(int, sys.stdin.readline().strip().split()))
line = []
for i in range(n):
    line.insert(temp[i],i+1)
res = " ".join(str(i) for i in line[::-1])
print(res)