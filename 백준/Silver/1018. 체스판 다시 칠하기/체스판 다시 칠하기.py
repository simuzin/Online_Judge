import sys

n,m = map(int, sys.stdin.readline().strip().split())
key = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
temp, count =[], []
for _ in range(n):
    temp.append(sys.stdin.readline().strip())
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = 0
        for k in range(8):
            for o in range(8):
                if temp[i+k][j+o] == key[k][o]:
                    cnt += 1
        count.append(min(cnt, 64-cnt))
print(min(count))