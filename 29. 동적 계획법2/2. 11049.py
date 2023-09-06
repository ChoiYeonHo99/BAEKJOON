import sys
MAX = 2**31 - 1

N = int(sys.stdin.readline().rstrip())
dp = [[0] * (N+1) for _ in range(N+1)]

matrix = [[]]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

for gap in range(1,N):
    for i in range(1,N-gap+1):
        j = i + gap
        dp[i][j] = MAX
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], (dp[i][k] + dp[k + 1][j] + (matrix[i][0] * matrix[k][1] * matrix[j][1])))

print(dp[1][N])