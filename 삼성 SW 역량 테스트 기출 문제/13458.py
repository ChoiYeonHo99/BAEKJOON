import sys
import math

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

count = 0
for i in range(N):
    remain = A[i] - B
    if remain > 0:
        count += 1 + math.ceil(remain / C)
    else:
        count += 1

print(count)