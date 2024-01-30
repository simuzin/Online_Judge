import sys
l,p = map(int,sys.stdin.readline().strip().split())
news = list(map(int,sys.stdin.readline().strip().split()))
key = l*p
temp = []
for num in news:
    temp.append(num - key)
res = ' '.join(str(i) for i in temp)
print(res)