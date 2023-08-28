import sys

INF = float('inf')

def bellman(r: int):
    distance[r] = 0
    for _ in range(1, N+1):
        for u, v, w in edge:
            if distance[u] != INF and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    for _ in range(1, N+1):
        for u, v, w in edge:
            if distance[u] != INF and distance[v] > distance[u] + w:
                return -1

N, M = map(int, sys.stdin.readline().rstrip().split())
distance = [INF] * (N+1)
edge = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    edge.append((A, B, C))

if bellman(1) == -1:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)