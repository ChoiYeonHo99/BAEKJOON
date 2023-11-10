import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
nodeIn = [[] for _ in range(N+1)]
nodeOut = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    nodeIn[v].append(u)
    nodeOut[u].append(v)

q = deque()
result = []
for i in range(1, N+1):
    if len(nodeIn[i]) == 0:
        q.append(i)
        visited[i] = True

while q:
    node = q.popleft()
    result.append(node)
    for x in nodeOut[node]:
        nodeIn[x].remove(node)
        if len(nodeIn[x]) == 0 and not visited[x]:
            q.append(x)
            visited[x] = True
    nodeOut[node].clear()

print(*result)