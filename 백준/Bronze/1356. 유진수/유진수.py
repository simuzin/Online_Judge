import sys
from math import prod
n = sys.stdin.readline().strip()
flag = 0
for i in range(1,len(n)):
    a = [int(j) for j in n[:i]]
    b = [int(j) for j in n[i:]]
    if prod(a) == prod(b):
        print("YES")
        flag += 1
        break
if flag == 0:
    print("NO")
