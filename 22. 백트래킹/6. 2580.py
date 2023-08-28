import sys

board = []
blank = []
for i in range(9):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(line)
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])

def row(y: int, n: int):
    for i in range(9):
        if board[y][i] == n:
            return False
    return True

def col(x: int, n: int):
    for i in range(9):
        if board[i][x] == n:
            return False
    return True

def box(x: int, y: int, n: int):
    ty = y//3*3
    tx = x//3*3
    for i in range(3):
        for j in range(3):
            if board[ty+i][tx+j] == n:
                return False
    return True

def sudoku(index: int):
    if index == len(blank):
        for i in range(9):
            print(' '.join(map(str, board[i])))
        return True
    
    y = blank[index][0]
    x = blank[index][1]
    for i in range(1, 10):
        if row(y, i) and col(x, i) and box(x, y, i):
            board[y][x] = i
            if sudoku(index+1):
                return True
            board[y][x] = 0
    return False

sudoku(0)