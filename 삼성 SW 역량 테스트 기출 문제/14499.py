import sys

def move(d: int):
    if d == 4:
        temp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = temp
    elif d == 3:
        temp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i-1][1]
        dice[0][1] = temp
    elif d == 1:
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    elif d == 2:
        temp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = temp

N, M, x, y, K = map(int, sys.stdin.readline().rstrip().split())
world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().rstrip().split())))
commands = list(map(int, sys.stdin.readline().rstrip().split()))
dice = [[0] * 3 for _ in range(4)]

direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
for i in range(K):
    dx, dy = direction[commands[i]]
    if 0 > x + dx or x + dx > N - 1 or 0 > y + dy or y + dy > M - 1:
        continue
    else:
        x += dx
        y += dy
        move(commands[i])
        if world[x][y] == 0:
            world[x][y] = dice[3][1]
        else:
            dice[3][1] = world[x][y]
            world[x][y] = 0
        print(dice[1][1])