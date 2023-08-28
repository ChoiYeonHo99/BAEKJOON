import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

dp[1] = 0
if n >= 2:
    dp[2] = 1
if n >= 3:
    dp[3] = 1

if n >= 4:
    for i in range(4, n+1):
        if i % 6 == 0:
            dp[i] = min(dp[i//2]+1, dp[i//3]+1, dp[i-1]+1, dp[i-2]+2)
        elif i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i-1]+1, dp[i-2]+2)
        elif i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i-1]+1, dp[i-2]+2)
        else:
            dp[i] = min(dp[i-1]+1, dp[i-2]+2)

print(dp[n])