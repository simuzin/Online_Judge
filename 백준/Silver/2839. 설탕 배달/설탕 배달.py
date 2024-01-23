n = int(input())
dp = [float('inf')] * (n+1)
dp[0] = 0
for i in range(1,n+1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i-3] +1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5] +1)
print(dp[n] if dp[n] != float('inf') else -1)