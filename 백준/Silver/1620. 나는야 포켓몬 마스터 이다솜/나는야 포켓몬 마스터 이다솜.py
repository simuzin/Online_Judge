import sys
n,m = map(int,sys.stdin.readline().strip().split())
dogam_n, dogam_i = {}, {}
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    dogam_n[name] = i
    dogam_i[str(i)] = name
for _ in range(m):
    temp = sys.stdin.readline().strip()
    if temp.isalpha():
        print(dogam_n[temp])
    else:
        print(dogam_i[temp])