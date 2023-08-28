import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0, 1, True)])
    visited[0][0] = True

    while queue:
        x, y, count, breaker = queue.popleft()

        if x == n-1 and y == m-1:
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if breaker:
                    if field[nx][ny] == 1 and not visited_breaker[nx][ny]:
                        queue.append((nx, ny, count+1, False))
                        visited_breaker[nx][ny] = True
                    elif field[nx][ny] == 0 and not visited[nx][ny]:
                        queue.append((nx, ny, count+1, breaker))
                        visited[nx][ny] = True
                else:
                    if field[nx][ny] == 0 and not visited_breaker[nx][ny]:
                        queue.append((nx, ny, count+1, breaker))
                        visited_breaker[nx][ny] = True

    return -1

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [[False] * m for _ in range(n)]
visited_breaker = [[False] * m for _ in range(n)]
field = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

answer = bfs()
print(answer)