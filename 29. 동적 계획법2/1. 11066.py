import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())

    chapter = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [[0] * k for _ in range(k)]
    for i in range(k-1):
        dp[i][i+1] = chapter[i] + chapter[i+1]      #두개씩 미리 더해줌

    accumulated_sum = [0] * (k+1)
    accumulated_sum[1] = chapter[0]
    for i in range(2, k+1):
        accumulated_sum[i] = accumulated_sum[i-1] + chapter[i-1]   #누적합 구해줌

    for i in range(2, k):                                                #길이가 3이상 부터 구해주기 위해 i=2부터 시작 ex)AB+C    -> 즉 i=2이면 3의 길이인 애들을 모두 구함
        for j in range(i, k):                                            #대각선 밑으로 내려가기 위한 for문
            minValue = 2 ** 31
            for x in range(j-i, j):                                      #(1,4)가 있으면 (1,1)+(2,4), (1,2)+(3,4), (1,3)+(4,4) 중에 최소값을 구함
                minValue = min(minValue, dp[j-i][x] + dp[x+1][j])
            dp[j-i][j] = minValue + (accumulated_sum[j+1] - accumulated_sum[j-i])      #구한 최소값과 누적합을 더해줌

    print(dp[0][k-1])