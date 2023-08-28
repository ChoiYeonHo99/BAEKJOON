import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y102):
    queue = deque([(x, y, 0)])
    visited[x][y] = True

    while queue:
        i, j, count = queue.popleft()

        if i == tx and j == ty:
            return count

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().rstrip().split())
    tx, ty = map(int, sys.stdin.readline().rstrip().split())
    visited = [[False] * n for _ in range(n)]

    answer = bfs(x, y, tx, ty)
    print(answer)