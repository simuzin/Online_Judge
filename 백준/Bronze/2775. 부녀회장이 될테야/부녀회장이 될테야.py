n = int(input())
for _ in range(n):
    k = int(input())
    n = int(input())
    temp = []
    for i in range(k+1):
        temp.append([])
        if i == 0:
            for j in range(1,n+1):
                temp[-1].append(j)
        else:
            for j in range(1,n+1):
                temp[-1].append(sum(temp[i-1][:j]))
    print(temp[k][n-1])