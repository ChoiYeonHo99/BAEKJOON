import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    day = 0

    while queue:
        x, y, count = queue.popleft()
        day = count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                queue.append((nx, ny, count + 1))
                tomato[nx][ny] = 1
                
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1
    return day

m, n = map(int, sys.stdin.readline().rstrip().split())
tomato = []
queue = deque([])
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    tomato.append(line)
    for j in range(m):
        if line[j] == 1:
            queue.append((i, j, 0))

answer = bfs()
print(answer)