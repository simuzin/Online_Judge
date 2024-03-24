import sys

n = int(sys.stdin.readline().strip())
temp = [False, False] + [True]*(1003002)

# 1000000 --> 1003002

for i in range(2,1003002):
    if temp[i] and (i >= n) and (str(i) == str(i)[::-1]):
        print(i)
        break
    for j in range(2*i,1003002,i):
        temp[j] = False