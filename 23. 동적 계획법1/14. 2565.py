import sys

n = int(sys.stdin.readline().rstrip())
line = []
for _ in range(n):
    i = list(map(int, sys.stdin.readline().rstrip().split()))
    line.append(i)
line.sort(key = lambda x:x[0])

line_b = []
for i in range(n):
    line_b.append(line[i][1])

dp = [0] * n

for i in range(n):
    for j in range(i):
        if line_b[i] > line_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))