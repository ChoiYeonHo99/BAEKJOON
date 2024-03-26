import sys
from collections import deque

def bfs():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    ladder = {}
    snake = {}
    for _ in range(n):
        s, e = map(int, sys.stdin.readline().rstrip().split())
        ladder[s] = e
    for _ in range(m):
        s, e = map(int, sys.stdin.readline().rstrip().split())
        snake[s] = e
    
    move = [1, 2, 3, 4, 5, 6]
    board = [0] * (101)
    visited = [False] * (101)
    visited[1] = True
    queue = deque([])
    queue.append((1, 0))

    while queue:
        position, count = queue.popleft()

        for i in range(6):
            nx = position + move[i]
            if nx > 100:
                break
            if nx == 100:
                return count + 1

            if nx in ladder:
                nx = ladder[nx]
            if nx in snake:
                nx = snake[nx]
            
            if not visited[nx]:
                visited[nx] = True
                board[nx] = count + 1
                queue.append((nx, count + 1))
            else:
                if board[nx] > count + 1:
                    board[nx] = count + 1
                    queue.append((nx, count + 1))
    return 0

print(bfs())