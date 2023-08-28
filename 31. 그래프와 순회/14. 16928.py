import sys
from collections import deque

def bfs():
    queue = deque([(1, 0)])
    visited[1] = True

    while queue:
        x, count = queue.popleft()

        if x == 100:
            return count
        
        for i in range(1, 7):
            if x+i < 101 and visited[x+i] == False:
                if x+i in node:
                    queue.append((node[x+i], count+1))
                    visited[node[x+i]] = True
                else:
                    queue.append((x+i, count+1))
                    visited[x+i] = True

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * 101
node = {}

for _ in range(n+m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u] = v

answer = bfs()
print(answer)