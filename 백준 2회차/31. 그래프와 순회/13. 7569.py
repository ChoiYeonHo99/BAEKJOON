import sys
from collections import deque

def bfs():
    m, n, h = map(int, sys.stdin.readline().rstrip().split())
    tomato = []
    queue = deque([])
    for k in range(h):
        tmp = []
        for i in range(n):
            tmp.append(list(map(int, sys.stdin.readline().rstrip().split())))
            for j in range(m):
                if tmp[i][j] == 1:
                    queue.append((k, i, j, 0))
        tomato.append(tmp)

    result = 0
    directionX = [1, 0, -1, 0, 0, 0]
    directionY = [0, 1, 0, -1, 0, 0]
    directionZ = [0, 0, 0, 0, 1, -1]

    while queue:
        z, x, y, day = queue.popleft()
        result = day

        for i in range(6):
            nz = z + directionZ[i]
            nx = x + directionX[i]
            ny = y + directionY[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = 1
                queue.append((nz, nx, ny, day+1))

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0:
                    result = -1

    return result

print(bfs())