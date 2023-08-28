import sys
INF = float('inf')

V, E =  map(int, sys.stdin.readline().rstrip().split())
distance = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w =  map(int, sys.stdin.readline().rstrip().split())
    distance[u][v] = w

for i in range(1, V+1):
    distance[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

cycle = INF
for i in range(1, V):
    for j in range(i+1, V+1):
        cycle = min(cycle, distance[i][j] + distance[j][i])

if cycle == INF:
    print("-1")
else:
    print(cycle)