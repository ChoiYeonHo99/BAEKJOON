import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
reverse_num_list = num_list[::-1]

dp = [0 for _ in range(n)]
reverse_dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
        if reverse_num_list[i] > reverse_num_list[j] and reverse_dp[i] < reverse_dp[j]:
            reverse_dp[i] = reverse_dp[j]
    dp[i] += 1
    reverse_dp[i] += 1

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = dp[i] + reverse_dp[n-i-1] - 1

print(max(result))