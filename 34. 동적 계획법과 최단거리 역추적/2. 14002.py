import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

length = [0] * N
trace = [[] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if length[i] < length[j] and A[i] > A[j]:
            length[i] = length[j]
            trace[i] = [] + trace[j]
    length[i] += 1
    trace[i].append(A[i])

maxValue = max(length)
index = length.index(maxValue)
print(maxValue)
print(*trace[index])