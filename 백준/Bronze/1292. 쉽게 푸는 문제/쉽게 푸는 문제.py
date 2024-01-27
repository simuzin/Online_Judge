import sys
x,y = map(int,sys.stdin.readline().strip().split())
temp, flag, i = [0]*y, 0, 1
while True:
    for _ in range(i):
        temp[flag] = i
        flag += 1
        if flag == y:
            break
    i += 1
    if flag == y:
        break
print(sum(temp[x-1:y]))