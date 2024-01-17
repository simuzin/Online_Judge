import sys
n = int(sys.stdin.readline().strip())
res = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().strip().split()))
    mean = (sum(temp) - temp[0]) / temp[0]
    cnt = 0
    for i in range(1, len(temp)):
        if mean < temp[i]:
            cnt += 1
    res.append(cnt/temp[0]*100)
for i in range(n):
    print(f'{res[i]}%')
