import sys
n = int(input())
step = [0]
for _ in range(n):
    score = int(sys.stdin.readline().strip())
    step.append(score)

dp = [0] * (n+1)
dp[0] = 0
if n >= 1:
    dp[1] = step[1]
if n >= 2:
    dp[2] = step[1] + step[2]
if n >= 3:
    dp[3] = max(step[1] + step[3], step[2] + step[3])
if n >= 4:
    for i in range(4,n+1):
        dp[i] = max(dp[i-2] + step[i], dp[i-3] + step[i-1] + step[i])
print(dp[n])