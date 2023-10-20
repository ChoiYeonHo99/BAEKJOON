import sys
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())
room = []
airpurifier = []
dust = []
for i in range(R):
    room.append(list(map(int, sys.stdin.readline().split())))
    for j in range(C):
        if room[i][j] == -1:
            airpurifier.append(i)

directionX = [1, 0, -1, 0]
directionY = [0, 1, 0, -1]
for _ in range(T):
    for i in range(R):
        for j in range(C):
            if room[i][j] != -1 and room[i][j] != 0:
                dust.append((i, j, room[i][j]))

    room = [[0] * C for _ in range(R)]
    room[airpurifier[0]][0] = -1
    room[airpurifier[1]][0] = -1

    while dust:
        x, y, n = dust.pop()
        count = 0
        for i in range(4):
            dx = directionX[i]
            dy = directionY[i]
            if 0 <= x+dx < R and 0 <= y+dy < C and room[x+dx][y+dy] != -1:
                count += 1
                room[x+dx][y+dy] += n // 5
        room[x][y] += n - (n // 5) * count
    
    if 0 <= airpurifier[0] - 1:
        room[airpurifier[0]-1][0] = 0
    for i in range(airpurifier[0]-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(C-1):
        room[0][i] = room[0][i+1]
    for i in range(airpurifier[0]):
        room[i][C-1] = room[i+1][C-1]
    for i in range(C-1, 1, -1):
        room[airpurifier[0]][i] = room[airpurifier[0]][i-1]
    if C >= 2:
        room[airpurifier[0]][1] = 0

    if airpurifier[1] + 1 < R:
        room[airpurifier[1]+1][0] = 0
    for i in range(airpurifier[1]+1, R-1):
        room[i][0] = room[i+1][0]
    for i in range(C-1):
        room[R-1][i] = room[R-1][i+1]
    for i in range(R-1, airpurifier[1], -1):
        room[i][C-1] = room[i-1][C-1]
    for i in range(C-1, 1, -1):
        room[airpurifier[1]][i] = room[airpurifier[1]][i-1]
    if C >= 2:
        room[airpurifier[1]][1] = 0

result = 2
for i in range(R):
    for j in range(C):
        result += room[i][j]
print(result)