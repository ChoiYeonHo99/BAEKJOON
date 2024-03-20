import sys

n = int(sys.stdin.readline().rstrip())
array = []
for i in range(1, n+1):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    tmp = [0] * (n-i)
    array.append(line + tmp)

dp = [[0] * n for _ in range(n)]
dp[0][0] = array[0][0]
for i in range(1, n):
    for j in range(i+1):
        if i > 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]
        else:
            dp[i][j] = dp[i-1][j] + array[i][j]

print(max(dp[n-1]))