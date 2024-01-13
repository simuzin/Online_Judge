import sys
n = int(sys.stdin.readline())
temp = []
for _ in range(n):
    a,b = sys.stdin.readline().split()
    temp.append([int(a), b])
answer = sorted(temp, key = lambda x:x[0])
for i in range(n):
    print(answer[i][0], answer[i][1])
