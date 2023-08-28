import sys
from collections import deque
sys.setrecursionlimit(10**4)

def dfs(R: int):
    dfs_visited[R] = True
    print(R, end = " ")

    for x in node[R]:
        if dfs_visited[x] == False:
            dfs(x)

def bfs(R: int):
    bfs_visited[R] = True
    print(R, end = " ")

    q.append(r)
    while len(q) != 0:
        u = q.popleft()
        for v in node[u]:
            if bfs_visited[v] == False:
                bfs_visited[v] = True
                print(v, end = " ")
                q.append(v)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
node = [[] for _ in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
q = deque([])

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1, n+1):
    node[i].sort()

dfs(r)
print()
bfs(r)