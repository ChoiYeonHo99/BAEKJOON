import sys

n = int(sys.stdin.readline().rstrip())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    dp[0][i] = 1
    dp[1][i] = 1

if n >= 2:
    for i in range(2, n+1):
        for j in range(1, 10):
            if j == 1:
                dp[i][j] = dp[i-1][j+1] + dp[i-2][j]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

sum = 0
for i in range(1, 10):
    sum += dp[n][i]
print(sum % 1000000000)