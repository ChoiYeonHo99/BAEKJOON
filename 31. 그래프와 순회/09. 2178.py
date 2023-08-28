import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m):
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        x, y, count = queue.popleft()

        if x == n-1 and y == m-1:
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True

n, m = map(int, sys.stdin.readline().rstrip().split())
field = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = bfs(n, m)
print(answer)