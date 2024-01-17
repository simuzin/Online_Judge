import sys
temp, long = [], 0
for i in range(5):
    temp.append(sys.stdin.readline().strip())
    if long < len(temp[-1]):
        long = len(temp[-1])
for i in range(long):
    for j in range(5):
        if i < len(temp[j]):
            print(temp[j][i], end = '')