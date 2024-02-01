import sys
key = []
for _ in range(9):
    temp = list(map(int,sys.stdin.readline().strip().split()))
    for n in temp:
        key.append(n)
i = key.index(max(key))
print(max(key))
print(i//9+1, i%9+1)