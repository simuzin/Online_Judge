import sys

n,k = map(int, sys.stdin.readline().strip().split())
temp = [False, False] + [True]*(n+1)
prime = []

for i in range(2, n+1):
    if temp[i]:
        prime.append(i)
    for j in range(i, n+1, i):
        if temp[j]:
            temp[j] = False
            k -= 1
            if k == 0:
                print(j)
                break