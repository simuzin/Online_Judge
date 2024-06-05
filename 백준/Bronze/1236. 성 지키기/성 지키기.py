import sys
n,m = map(int, sys.stdin.readline().strip().split())
row_cnt, column_cnt = 0, [False] * m
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    for j in range(m):
        if temp[j] == 'X':
            column_cnt[j] = True
    if 'X' in temp:
        row_cnt += 1
print(max(n - row_cnt, m - sum(column_cnt)))