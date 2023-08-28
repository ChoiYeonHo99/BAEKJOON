import sys

n = int(sys.stdin.readline().rstrip())
step = [0]

for _ in range(n):
    step.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (n + 1)
dp[1] = step[1]
if n >= 2:
    dp[2] = step[1] + step[2]
if n >= 3:
    dp[3] = max(step[1] + step[3], step[2] + step[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])

print(dp[n])