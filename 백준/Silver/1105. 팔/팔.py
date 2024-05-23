import sys

l, r = map(list, sys.stdin.readline().strip().split())
temp, cnt = 0, 0
if len(l) == len(r):
    for i in range(len(l)):
        if l[i] == r[i]:
            temp += 1
            if (i+1 == temp) and (l[i] == '8'):
                cnt += 1
        else:
            break
print(cnt)