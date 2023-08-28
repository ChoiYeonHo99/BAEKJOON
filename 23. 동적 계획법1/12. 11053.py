import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))