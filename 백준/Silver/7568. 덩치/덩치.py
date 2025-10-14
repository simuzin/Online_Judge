import sys
input = sys.stdin.readline

N = int(input().strip())
dongchi_list = []
result = []
for i in range(N):
    x, y = map(int, input().split())
    dongchi_list.append((x,y))

for i in range(N):
    x, y = dongchi_list[i]
    count = 0
    for j in range(N):
        p,q = dongchi_list[j]
        if x < p and y < q:
            count += 1
    result.append(count+1)

print(*result)