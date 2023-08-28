import sys
from collections import deque

def bfs(r: int):
    visited = [False] * (n+1)
    que = deque()
    global maxValue, maxNode

    visited[r] = True
    que.append((0, r))

    while que:
        distance, u = que.popleft()
        if distance > maxValue:
            maxValue = distance
            maxNode = u

        for w, v in node[u]:
            if not visited[v]:
                visited[v] = True
                que.append((distance + w, v))

n = int(sys.stdin.readline().rstrip())
node = [[] for _ in range(n+1)]
maxValue = 0
maxNode = 0

for _ in range(n-1):
    a, b, d = map(int, sys.stdin.readline().rstrip().split())
    node[a].append((d, b))
    node[b].append((d, a))

bfs(1)

bfs(maxNode)

print(maxValue)