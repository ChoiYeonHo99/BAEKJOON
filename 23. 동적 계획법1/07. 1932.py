import sys

n = int(sys.stdin.readline().rstrip())
triangle = []

for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    triangle.append(line)

dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))