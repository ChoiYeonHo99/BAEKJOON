import sys

def move(x: int, y: int, num: int, total: int):
    global result
    if result >= total + max_val * (3 - num):
        return

    if num == 3:
        result = max(result, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            if num == 1:
                visited[nx][ny] = True
                move(x, y, num+1, total+board[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            move(nx, ny, num+1, total+board[nx][ny])
            visited[nx][ny] = False

N, M = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0
max_val = max(map(max, board))
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        move(i, j, 0, board[i][j])
        visited[i][j] = False

print(result)