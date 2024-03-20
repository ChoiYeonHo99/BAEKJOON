import sys

n = int(sys.stdin.readline().rstrip())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

dp = [0] * n
dp[0] = array[0]
if n >= 2:
    dp[1] = array[0] + array[1]
if n >= 3:
    dp[2] = max(array[0] + array[2], array[1] + array[2])
for i in range(3, n):
    dp[i] = max(dp[i-3] + array[i-1] + array[i], dp[i-2] + array[i])
    
print(dp[n-1])