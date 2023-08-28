import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
parent = {}
visited = [False] * (n+1)
node = [[] for _ in range(n+1)]
que = deque()
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b)
    node[b].append(a)

visited[1] = True
que.append(1)
while que:
    r = que.popleft()

    for x in node[r]:
        if not visited[x]:
            visited[x] = True
            parent[x] = r
            que.append(x)

for i in range(2, n+1):
    print(parent[i])