import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
n = 0
n1 = len(s1)
n2 = len(s2)
if n1 > n2:
    n = n1
else:
    n = n2
dp = [0 for _ in range(n)]

for i in range(n1):
    count = 0
    for j in range(n2):
        if count < dp[j]:
            count = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = count + 1

print(max(dp))