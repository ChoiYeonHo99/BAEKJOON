import sys

m = int(sys.stdin.readline())
f = [0] + list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())

sparseTable = [[0] * (19) for _ in range(m+1)]
for i in range(1, m+1):
    sparseTable[i][0] = f[i]

for j in range(1, 19):
    for i in range(1, m+1):
        sparseTable[i][j] = sparseTable[sparseTable[i][j-1]][j-1]

for _ in range(Q):
    n, x = map(int, sys.stdin.readline().split())
    for i in range(18, -1, -1):
        if n >= 2**i:
            n -= 2**i
            x = sparseTable[x][i]

    print(x)