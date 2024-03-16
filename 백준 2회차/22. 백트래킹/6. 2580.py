import sys

def check(x: int, y: int, a: int):
    for i in range(9):
        if board[i][y] == a:
            return False
    for i in range(9):
        if board[x][i] == a:
            return False

    mx = x // 3 * 3
    my = y // 3 * 3
    for i in range(mx , mx + 3):
        for j in range(my, my + 3):
            if board[i][j] == a:
                return False

    return True

def sudoku(n: int):
    if n == len(blank):
        for i in range(9):
            print(*board[i])
        return True

    x, y = blank[n]
    for i in range(1, 10):
        if check(x, y, i):
            board[x][y] = i
            if sudoku(n+1):
                return True
            board[x][y] = 0
    return False

board = []
blank = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

sudoku(0)