import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    
    dp1 = [0] * (n+1)
    dp0 = [0] * (n+1)
    if n >= 0:
        dp1[0] = 0
        dp0[0] = 1
    if n >=1:
        dp1[1] = 1
        dp0[1] = 0
    for i in range(2,n+1):
        dp1[i] = dp1[i-2] + dp1[i-1]
        dp0[i] = dp0[i-2] + dp0[i-1]
    print(dp0[n], dp1[n])
