import sys
import copy

def move(d):
    block = [[False] * N for _ in range(N)]

    if d == "right":
        for i in range(N):
            for j in range(N-2, -1, -1):
                if board[i][j] == 0:
                    continue

                k = j
                while board[i][k+1] == 0 or (board[i][k+1] == board[i][k] and block[i][k] == False and block[i][k+1] == False):
                    if board[i][k+1] == 0:
                        board[i][k+1] = board[i][k]
                        board[i][k] = 0
                    else:
                        board[i][k+1] *= 2
                        board[i][k] = 0
                        block[i][k+1] = True
                    k += 1
                    if k >= N-1:
                        break
    elif d == "left":
        for i in range(N):
            for j in range(1, N):
                if board[i][j] == 0:
                    continue

                k = j
                while board[i][k-1] == 0 or (board[i][k-1] == board[i][k] and block[i][k] == False and block[i][k-1] == False):
                    if board[i][k-1] == 0:
                        board[i][k-1] = board[i][k]
                        board[i][k] = 0
                    else:
                        board[i][k-1] *= 2
                        board[i][k] = 0
                        block[i][k-1] = True
                    k -= 1
                    if k <= 0:
                        break
    elif d == "up":
        for i in range(N):
            for j in range(1, N):
                if board[j][i] == 0:
                    continue

                k = j
                while board[k-1][i] == 0 or (board[k-1][i] == board[k][i] and block[k][i] == False and block[k-1][i] == False):
                    if board[k-1][i] == 0:
                        board[k-1][i] = board[k][i]
                        board[k][i] = 0
                    else:
                        board[k-1][i] *= 2
                        board[k][i] = 0
                        block[k-1][i] = True
                    k -= 1
                    if k <= 0:
                        break
    elif d == "down":
        for i in range(N):
            for j in range(N-2, -1, -1):
                if board[j][i] == 0:
                    continue

                k = j
                while board[k+1][i] == 0 or (board[k+1][i] == board[k][i] and block[k][i] == False and block[k+1][i] == False):
                    if board[k+1][i] == 0:
                        board[k+1][i] = board[k][i]
                        board[k][i] = 0
                    else:
                        board[k+1][i] *= 2
                        board[k][i] = 0
                        block[k+1][i] = True
                    k += 1
                    if k >= N-1:
                        break

N = int(sys.stdin.readline().rstrip())
original = []
for _ in range(N):
    original.append(list(map(int, sys.stdin.readline().rstrip().split())))

direction = ["left", "right", "up", "down"]
result = 0
for a in direction:
    for b in direction:
        for c in direction:
            for d in direction:
                for e in direction:
                    board = copy.deepcopy(original)
                    move(a)
                    move(b)
                    move(c)
                    move(d)
                    move(e)
                    for i in range(N):
                        value = max(board[i])
                        result = max(result, value)

print(result)