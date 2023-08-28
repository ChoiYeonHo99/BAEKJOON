import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    day = 0

    while queue:
        z, x, y, count = queue.popleft()
        day = count

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and tomato[nz][nx][ny] == 0:
                queue.append((nz, nx, ny, count + 1))
                tomato[nz][nx][ny] = 1

    for k in range(h):     
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 0:
                    return -1
    return day



m, n, h = map(int, sys.stdin.readline().rstrip().split())
tomato = []
queue = deque([])
for k in range(h):
    board = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        board.append(line)
        for j in range(m):
            if line[j] == 1:
                queue.append((k, i, j, 0))
    tomato.append(board)

answer = bfs()
print(answer)