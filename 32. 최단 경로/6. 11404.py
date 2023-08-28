import sys

INF = float('inf')

n = int(sys.stdin.readline().rstrip())
node = [[INF] * (n+1) for _ in range(n+1)]

m = int(sys.stdin.readline().rstrip())
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    node[a][b] = min(node[a][b], c)
for i in range(1, n+1):
    node[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            node[i][j] = min(node[i][j], node[i][k]+node[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if node[i][j] != INF:
            print(node[i][j], end = " ")
        else:
            print(0, end = " ")
    print()