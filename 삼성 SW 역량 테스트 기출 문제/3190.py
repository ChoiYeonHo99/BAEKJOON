import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
board = [[0] * (N+2) for _ in range(N+2)]
for i in range(N+2):
    board[0][i] = 1
    board[N+1][i] = 1
for i in range(N+2):
    board[i][0] = 1
    board[i][N+1] = 1
for _ in range(K):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    board[i][j] = 2

L = int(sys.stdin.readline().rstrip())
command = deque()
for _ in range(L):
    X, C = sys.stdin.readline().rstrip().split()
    command.append((int(X), C))

snake = deque()
snake.append((1, 1))
board[1][1] = 1
directionX = [0, 1, 0, -1]
directionY = [1, 0, -1, 0]
index = 0
t = 0
gameover = 0
while command:
    a, b = command.popleft()
    while t < a:
        t += 1
        x, y = snake.popleft()
        x += directionX[index]
        y += directionY[index]
        if board[x][y] == 2:
            board[x][y] = 1
            snake.appendleft((x-directionX[index], y-directionY[index]))
            snake.appendleft((x, y))
        elif board[x][y] == 0:
            board[x][y] = 1
            snake.appendleft((x-directionX[index], y-directionY[index]))
            snake.appendleft((x, y))
            i, j = snake.pop()
            board[i][j] = 0
        else:
            gameover = t
            break

    if gameover != 0:
        break
    if b == "L":
        index -= 1
    else:
        index += 1
    index %= 4

if gameover != 0:
    print(gameover)
else:
    while True:
        t += 1
        x, y = snake.popleft()
        x += directionX[index]
        y += directionY[index]
        if board[x][y] == 2:
            board[x][y] = 1
            snake.appendleft((x-directionX[index], y-directionY[index]))
            snake.appendleft((x, y))
        elif board[x][y] == 0:
            board[x][y] = 1
            snake.appendleft((x-directionX[index], y-directionY[index]))
            snake.appendleft((x, y))
            i, j = snake.pop()
            board[i][j] = 0
        else:
            gameover = t
            break
    print(gameover)