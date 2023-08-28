import sys

n = int(sys.stdin.readline().rstrip())
num_array = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * n
dp[0] = num_array[0]
maxValue = dp[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + num_array[i], num_array[i])
    if maxValue < dp[i]:
        maxValue = dp[i]

print(maxValue)