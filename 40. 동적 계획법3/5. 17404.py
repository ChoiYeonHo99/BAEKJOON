import sys
MAX = float('inf')

n = int(sys.stdin.readline().rstrip())
rgb = []
result = MAX

for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    rgb.append(line)

for i in range(3):
    dp = [[MAX] * 3 for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])
    
    for j in range(3):
        if i != j:
            result = min(result, dp[n-1][j])

print(result)