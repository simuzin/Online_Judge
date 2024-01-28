import sys
n = int(sys.stdin.readline().strip())
for i in range(1,n+1):
    temp = list(map(str,sys.stdin.readline().strip().split()))
    res = ' '.join(temp[::-1])
    print(f'Case #{i}: {res}')