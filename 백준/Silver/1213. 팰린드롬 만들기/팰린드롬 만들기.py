import sys
from collections import Counter

s = list(sys.stdin.readline().strip())
s_cnt = Counter(s)
s_list = []

odd_count, temp = 0, ''
for i in s_cnt:
    if s_cnt[i] % 2 == 1:
        odd_count += 1
        temp = i
    
    for j in range(s_cnt[i] // 2):
            s_list.append(i)  
s_list.sort()

if odd_count > 1:
    print("I'm Sorry Hansoo")
elif odd_count == 0:
    answer = s_list + s_list[::-1]
    print(''.join(answer))
else:
    answer = s_list + list(temp) + s_list[::-1]
    print(''.join(answer))