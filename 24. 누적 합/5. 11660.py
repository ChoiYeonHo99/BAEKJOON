import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

sum_board = [[0] * n for _ in range(n)]
for i in range(n):
    sum = 0
    for j in range(n):
        sum += board[i][j]
        if i == 0:
            sum_board[i][j] = sum
        else:
            sum_board[i][j] = sum_board[i-1][j] + sum

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    if x1 == 1 and y1 == 1:
        print(sum_board[x2-1][y2-1])
    elif x1 == 1:
        print(sum_board[x2-1][y2-1] - sum_board[x2-1][y1-1-1])
    elif y1 == 1:
        print(sum_board[x2-1][y2-1] - sum_board[x1-1-1][y2-1])
    else:
        print(sum_board[x2-1][y2-1] - sum_board[x2-1][y1-1-1] - sum_board[x1-1-1][y2-1] + sum_board[x1-1-1][y1-1-1])