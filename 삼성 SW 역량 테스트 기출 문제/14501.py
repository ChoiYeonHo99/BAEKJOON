import sys

N = int(sys.stdin.readline().rstrip())
TP = []
for i in range(N):
    TP.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [0] * (N+1)
for i in range(N):
    for j in range(i + TP[i][0], N+1):
        if dp[j] < dp[i] + TP[i][1]:
            dp[j] = dp[i] + TP[i][1]

print(dp[N])