import sys
from collections import deque

def bfs():
    m, n = map(int, sys.stdin.readline().rstrip().split())
    tomato = []
    queue = deque([])
    for i in range(n):
        tomato.append(list(map(int, sys.stdin.readline().rstrip().split())))
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append((i, j, 0))

    result = 0
    directionX = [1, 0, -1, 0]
    directionY = [0, 1, 0, -1]

    while queue:
        x, y, day = queue.popleft()
        result = day

        for i in range(4):
            nx = x + directionX[i]
            ny = y + directionY[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                queue.append((nx, ny, day+1))

    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                result = -1

    return result

print(bfs())