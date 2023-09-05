import sys

N, M = map(int, sys.stdin.readline().strip().split())
memory = [0] + list(map(int, sys.stdin.readline().strip().split()))
cost = [0] + list(map(int, sys.stdin.readline().strip().split()))

maximum = sum(cost)
dp = [[0] * (maximum + 1) for _ in range(N + 1)]

result = maximum
for i in range(1, N+1):
    for j in range(maximum+1):
        if cost[i] <= j:
            dp[i][j] = max(memory[i] + dp[i-1][j - cost[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M:
            result = min(result, j)

print(result)