import sys

n_list = []
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    n_list.append(n)

prime, n_max = [], max(n_list)
temp = [False, False] + [True] * (2*n_max +1)
for i in range(2, 2*n_max+1):
    if temp[i]:
        prime.append(i)
    for j in range(i*2, 2*n_max+1, i):
        temp[j] = False

for i in n_list:
    cnt = 0
    for j in prime:
        if i < j <= 2*i:
            cnt += 1
    print(cnt)