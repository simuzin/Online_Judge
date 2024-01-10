n = int(input())
temp = list(map(int,input().split()))
m = max(temp)
for i in range(n):
    temp[i] = temp[i]/m*100
print(sum(temp)/n)