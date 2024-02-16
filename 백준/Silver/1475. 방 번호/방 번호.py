import sys
n = sys.stdin.readline().strip()
cnt = [0,0,0,0,0,0,0,0,0,0]
for num in n:
    cnt[int(num)] += 1
if abs(cnt[6] - cnt[9]) >= 2 :
    temp = (cnt[6] + cnt[9]) // 2
    if (cnt[6] + cnt[9]) % 2 == 0:
        cnt[6], cnt[9] = temp, temp
    else:
        cnt[6], cnt[9] = temp+1, temp
print(max(cnt))
