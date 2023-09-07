import sys
from bisect import bisect_left
from collections import deque

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A_index = [0] * N
K = [A[0]]

for i in range(1, N):
    if K[len(K)-1] < A[i]:
        A_index[i] = len(K)
        K.append(A[i])
    else:
        index = bisect_left(K, A[i])
        K[index] = A[i]
        A_index[i] = index

print(len(K))
target = len(K)-1
result = deque()
for i in range(N-1, -1, -1):
    if A_index[i] == target:
        result.appendleft(A[i])
        target -= 1
        if target == -1:
            break
print(*result)