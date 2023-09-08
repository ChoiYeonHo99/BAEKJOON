import sys

s1 = " " + sys.stdin.readline().rstrip()
s2 = " " + sys.stdin.readline().rstrip()

dp = [[0] * len(s2) for _ in range(len(s1))]
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

maxValue = 0
x = 0
y = 0
for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if dp[i][j] > maxValue:
            maxValue = dp[i][j]
            x = i
            y = j

result = []
target = maxValue
while dp[x][y] != 0:
    if dp[x-1][y] == target:
        x -= 1
        continue
    if dp[x][y-1] == target:
        y -= 1
        continue
    result.append(s1[x])
    x -= 1
    y -= 1
    target = dp[x][y]
result.reverse()

print(maxValue)
for i in range(maxValue):
    print(result[i], end = "")