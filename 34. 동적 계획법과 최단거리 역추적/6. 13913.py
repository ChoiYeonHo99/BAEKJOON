import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [100000] * (100002)
dp[N] = 0
index = [0] * (100001)
index[N] = N

if N >= K:
    print(N - K)
    for i in range(N, K-1, -1):
        print(i, end = " ")
else:
    for i in range(N-1, -1, -1):
        dp[i] = dp[i+1] + 1
        index[i] = i+1

    for i in range(N+1, 100001):
        if i % 2 == 0:
            dp[i] = dp[i//2] + 1
            index[i] = i//2
        else:
            dp[i+1] = dp[(i+1)//2] + 1
            index[i+1] = (i+1)//2

        if dp[i] > min(dp[i+1], dp[i-1]) + 1:
            if dp[i+1] > dp[i-1]:
                dp[i] = dp[i-1] + 1
                index[i] = i-1
            else:
                dp[i] = dp[i+1] + 1
                index[i] = i+1

    print(dp[K])
    a = K
    result = []
    while a != N:
        result.append(a)
        a = index[a]
    result.append(a)
    result.reverse()
    for i in range(len(result)):
        print(result[i], end = " ")