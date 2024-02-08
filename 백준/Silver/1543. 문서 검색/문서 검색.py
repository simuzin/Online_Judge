import sys
d = sys.stdin.readline().strip()
k = list(sys.stdin.readline().strip())
temp, cnt = [], 0
for c in d:
    temp.append(c)
    if temp[-(len(k)):] == k:
        cnt += 1
        for _ in range(len(k)):
            temp = []
print(cnt)