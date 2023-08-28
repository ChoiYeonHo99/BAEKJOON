import sys

def dfs(x: int, y: int):
    global size_count
    size_count += 1
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
    if y < n-1:
        if field[x][y+1] == 1 and visited[x][y+1] == False:
            dfs(x, y+1)

n = int(sys.stdin.readline().rstrip())
sys.setrecursionlimit(n**3)
field = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
node = []
size = []
size_count = 0
total = 0

for i in range(n):
    line = sys.stdin.readline().rstrip()
    for j in range(n):
        field[i][j] = int(line[j])
        if field[i][j] == 1:
            node.append((i, j))

while len(node) > 0:
    size_count = 0
    a = node.pop()
    x = a[0]
    y = a[1]
    if visited[x][y] == False:
        dfs(x, y)
        total += 1
        size.append(size_count)

print(total)
size.sort()
for i in size:
    print(i)