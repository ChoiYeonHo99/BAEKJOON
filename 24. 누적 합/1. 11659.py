import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
sum_list = [0 for _ in range(n)]
sum_list[0] = num_list[0]

for i in range(1, n):
    sum_list[i] = sum_list[i-1] + num_list[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == j:
        print(num_list[i-1])
    else:
        if i - 2 < 0:
            print(sum_list[j-1])
        else:
            print(sum_list[j-1] - sum_list[i-2])