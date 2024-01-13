import sys
k = int(sys.stdin.readline())
temp = []
for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        temp.pop()
    else:
        temp.append(n)
print(sum(temp))