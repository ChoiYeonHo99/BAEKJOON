import sys

n = int(sys.stdin.readline().rstrip())
global count
count = 0
chessboard = []
row = [True] * n

def nQueen(y: int):
    global count
    if len(chessboard) == n:
        count += 1
    elif y >= n:
        return
    else:
        for i in range(n):
            if row[i]:
                if checkTruePosition(i, y):
                    row[i] = False
                    chessboard.append([i, y])
                    nQueen(y+1)
                    row[i] = True
                    chessboard.pop()

def checkTruePosition(x: int, y: int):
    if len(chessboard) == 0:
        return True
    for i in chessboard:
        if abs(i[0] - x) == abs(i[1] - y):
            return False
    return True

nQueen(0)
print(count)