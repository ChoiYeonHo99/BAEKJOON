import sys
from collections import deque

def bfs():
    directionX = [1, 0, -1, 0]
    directionY = [0, 1, 0, -1]
    queue = deque([])
    queue.append((0, 0, 0, 1))
    wall = []
    n, m = map(int, sys.stdin.readline().rstrip().split())
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    visited_b = [[False] * m for _ in range(n)]
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        tmp = []
        for i in range(m):
            tmp.append(int(line[i]))
        wall.append(tmp)

    while queue:
        x, y, b, count = queue.popleft()
        if x == n - 1 and y == m - 1:
            return count

        for i in range(4):
            nx = x + directionX[i]
            ny = y + directionY[i]

            if 0 <= nx < n and 0 <= ny < m:
                if b == 0:
                    if not visited[nx][ny]:
                        if wall[nx][ny] == 1 and b == 0:
                            visited_b[nx][ny] = True
                            queue.append((nx, ny, 1, count + 1))
                        if wall[nx][ny] == 0:
                            visited[nx][ny] = True
                            queue.append((nx, ny, b, count + 1))
                else:
                    if not visited_b[nx][ny]:
                        if wall[nx][ny] == 0:
                            visited_b[nx][ny] = True
                            queue.append((nx, ny, b, count + 1))
    return -1

print(bfs())