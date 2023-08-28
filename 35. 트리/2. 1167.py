import sys
from collections import deque

def bfs(r: int):
    visited = [False] * (V+1)
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

V = int(sys.stdin.readline().rstrip())
node = [[] for _ in range(V+1)]
maxValue = 0
maxNode = 0

for _ in range(V):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    a = line[0]
    i = 1
    while line[i] != -1:
        b = line[i]
        d = line[i+1]
        node[a].append((d, b))
        node[b].append((d, a))
        i += 2

bfs(1)

bfs(maxNode)

print(maxValue)