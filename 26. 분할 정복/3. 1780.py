import sys

def check1(size: int):
    if size > n:
        return
    for i in range(0, n, size):
        for j in range(0, n, size):
            check2(i, j, size)
    check1(size * 3)

def check2(x: int, y: int, size: int):
    global plus, minus, zero
    color = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != paper[i][j]:
                return
    if color == 1:
        plus -= 8
    elif color == -1:
        minus -= 8
    else:
        zero -= 8

n = int(sys.stdin.readline().rstrip())
paper = []
plus = 0
minus = 0
zero = 0
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if paper[i][j] == 1:
            plus += 1
        elif paper[i][j] == -1:
            minus += 1
        else:
            zero += 1

check1(3)
print(minus)
print(zero)
print(plus)