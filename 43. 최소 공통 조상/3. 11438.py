import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
depth = [0] * (N+1)
parent = [[0] * 20 for _ in range(N+1)]
visited = [False] * (N+1)
node = [[] for _ in range(N+1)]
que = deque()
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b)
    node[b].append(a)

visited[1] = True
que.append((1, 0))
while que:
    r, d = que.popleft()
    depth[r] = d

    for x in node[r]:
        if not visited[x]:
            visited[x] = True
            parent[x][0] = r
            que.append((x, d+1))

for j in range(1, 20):
    for i in range(1, N+1):
        parent[i][j] = parent[parent[i][j-1]][j-1]

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(19, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = parent[b][i]

    if a == b:
        print(a)
        continue

    for i in range(19, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    print(parent[a][0])