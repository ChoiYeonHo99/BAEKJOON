import sys
sys.setrecursionlimit(10**6)

def dfs(R: int):
    visited[R] = True

    for x in node[R]:
        if visited[x] == False:
            dfs(x)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
node = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u].append(v)
    node[v].append(u)

dfs(1)
count = 0
for i in range(2, n+1):
    if visited[i]:
        count += 1
print(count)