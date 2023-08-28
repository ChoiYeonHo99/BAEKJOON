import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

m, k = map(int, sys.stdin.readline().rstrip().split())
b = []
for _ in range(m):
    b.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            result[i][j] += a[i][x] * b[x][j]

for x in result:
    print(*x)