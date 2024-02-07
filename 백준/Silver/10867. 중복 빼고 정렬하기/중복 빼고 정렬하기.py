import sys
n = int(sys.stdin.readline().strip())
temp = list(set(map(int,sys.stdin.readline().strip().split())))
temp.sort()
print(*temp)