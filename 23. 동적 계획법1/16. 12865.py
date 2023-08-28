import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
obj = [[0] * 2 for _ in range(n)]
for i in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    obj[i][0] = w
    obj[i][1] = v

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    weight = obj[i-1][0]
    value = obj[i-1][1]
    for j in range(1, k+1):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])