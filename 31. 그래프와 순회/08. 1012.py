import sys

def dfs(x: int, y: int):
    visited[x][y] = True
    if x > 0:
        if field[x-1][y] == 1 and visited[x-1][y] == False:
            dfs(x-1, y)
    if y > 0:
        if field[x][y-1] == 1 and visited[x][y-1] == False:
            dfs(x, y-1)
    if x < n-1:
        if field[x+1][y] == 1 and visited[x+1][y] == False:
            dfs(x+1, y)
    if y < m-1:
        if field[x][y+1] == 1 and visited[x][y+1] == False:
            dfs(x, y+1)

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    sys.setrecursionlimit(m * n * 10)
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    node = []
    total = 0

    for _ in range(k):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        field[i][j] = 1
        node.append((i, j))

    while len(node) > 0:
        a = node.pop()
        x = a[0]
        y = a[1]
        if visited[x][y] == False:
            dfs(x, y)
            total += 1

    print(total)