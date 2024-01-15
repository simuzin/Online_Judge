from collections import deque

n,k = map(int, input().split())
temp = [i for i in range(1,n+1)]
res, flag = [], k-1
while True:
    if temp:
        flag %= len(temp)
        res.append(temp.pop(flag))
        flag += k-1

    else:
        break
result = ", ".join(str(i) for i in res)
print(f'<{result}>')