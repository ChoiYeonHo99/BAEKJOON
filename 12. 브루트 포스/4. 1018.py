import sys

s = list(map(int, sys.stdin.readline().split()))
row = s[0]
column = s[1]
board = []
for i in range(row):
    board.append(sys.stdin.readline().rstrip())

min = 64
count = 0
for a in range(0, row-7):
    for b in range(0, column-7):
        for case in range(0, 2):
            for i in range(a, a+8):
                for j in range(b, b+8):
                    if case == 0:
                        if i % 2 == 0 and j % 2 == 0:
                            if board[i][j] != "W":
                                count += 1
                        elif i % 2 == 0 and j % 2 == 1:
                            if board[i][j] != "B":
                                count += 1
                        elif i % 2 == 1 and j % 2 == 0:
                            if board[i][j] != "B":
                                count += 1
                        elif i % 2 == 1 and j % 2 == 1:
                            if board[i][j] != "W":
                                count += 1
                    else:
                        if i % 2 == 0 and j % 2 == 0:
                            if board[i][j] != "B":
                                count += 1
                        elif i % 2 == 0 and j % 2 == 1:
                            if board[i][j] != "W":
                                count += 1
                        elif i % 2 == 1 and j % 2 == 0:
                            if board[i][j] != "W":
                                count += 1
                        elif i % 2 == 1 and j % 2 == 1:
                            if board[i][j] != "B":
                                count += 1
            if count < min:
                min = count
            count = 0
print(min)