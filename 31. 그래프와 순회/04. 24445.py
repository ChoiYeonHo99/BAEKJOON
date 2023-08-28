import sys
from collections import deque

def bfs(R: int):
    global count
    count += 1
    visited[R] = count

    q.append(r)
    while len(q) != 0:
        u = q.popleft()
        for v in node[u]:
            if visited[v] == 0:
                count += 1
                visited[v] = count
                q.append(v)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
node = [[] for _ in range(n+1)]
q = deque([])
visited = [0] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1, n+1):
    node[i].sort(reverse = True)

bfs(r)
for i in range(1, n+1):
    print(visited[i])