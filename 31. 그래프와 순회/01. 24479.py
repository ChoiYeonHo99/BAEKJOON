import sys
sys.setrecursionlimit(10**6)

def dfs(R: int):
    global count
    count += 1
    visited[R] = count

    for x in node[R]:
        if visited[x] == 0:
            dfs(x)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
node = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1, n+1):
    node[i].sort()

dfs(r)
for i in range(1, n+1):
    print(visited[i])