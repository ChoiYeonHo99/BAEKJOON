import sys
from collections import OrderedDict

def searchRoute(i: int, j: int):
    if len(route[i][j]) == 2:
        record.append(i)
        record.append(j)
    else:
        a, b, c = route[i][j]
        searchRoute(a, b)
        searchRoute(b, c)

INF = float('inf')

n = int(sys.stdin.readline().rstrip())
node = [[INF] * (n+1) for _ in range(n+1)]
route = [[0] * (n+1) for _ in range(n+1)]

m = int(sys.stdin.readline().rstrip())
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    node[a][b] = min(node[a][b], c)
    route[a][b] = (a, b)
for i in range(1, n+1):
    node[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if node[i][j] > node[i][k] + node[k][j]:
                node[i][j] = node[i][k] + node[k][j]
                route[i][j] = (i, k, j)

for i in range(1, n+1):
    for j in range(1, n+1):
        if node[i][j] == INF:
            print(0, end = " ")
        else:
            print(node[i][j], end = " ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or node[i][j] == INF:
            print(0)
        else:
            record = []
            searchRoute(i, j)
            result = list(OrderedDict.fromkeys(record))
            print(len(result), *result)