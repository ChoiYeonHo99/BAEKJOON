import sys
INF = float('inf')

N = int(sys.stdin.readline().rstrip())
distance = [INF] * (N+1)
distance[N] = 0
trace = [0] * (N+1)
for i in range(N, 0, -1):
    if i % 2 == 0:
        if distance[i // 2] > distance[i] + 1:
            distance[i // 2] = distance[i] + 1
            trace[i // 2] = i
    if i % 3 == 0:
        if distance[i // 3] > distance[i] + 1:
            distance[i // 3] = distance[i] + 1
            trace[i // 3] = i
    if distance[i - 1] > distance[i] + 1:
        distance[i - 1] = distance[i] + 1
        trace[i - 1] = i

index = 1
result = [1]
while trace[index] != 0:
    result.append(trace[index])
    index = trace[index]
result.reverse()

print(distance[1])
print(*result)