import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
sum = 0

for i in range(k):
    sum += num_list[i]
max = sum

for i in range(k, n):
    sum -= num_list[i-k]
    sum += num_list[i]
    if max < sum:
        max = sum

print(max)