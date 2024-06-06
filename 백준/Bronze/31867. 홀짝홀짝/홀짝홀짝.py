import sys

n = int(sys.stdin.readline().strip())
k = list(sys.stdin.readline().strip())
odd_cnt, even_cnt = 0, 0
for i in k:
    if int(i) % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

if odd_cnt > even_cnt:
    print("1")
elif odd_cnt < even_cnt:
    print("0")
else:
    print("-1")