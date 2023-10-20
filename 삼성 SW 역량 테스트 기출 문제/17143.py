import sys
from collections import deque

R, C, M = map(int, sys.stdin.readline().split())
ocean_move = [[deque() for _ in range(C+1)] for _ in range(R+1)]
ocean_fishing = [[deque() for _ in range(C+1)] for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    ocean_fishing[r][c].append((s, d, z))

directionX = [0, -1, 1, 0, 0]
directionY = [0, 0, 0, 1, -1]
result = 0
for fisherman in range(1, C+1):
    for i in range(1, R+1):
        if len(ocean_fishing[i][fisherman]) > 0:
            speed, direction, size = ocean_fishing[i][fisherman].pop()
            result += size
            break

    for i in range(1, R+1):
        for j in range(1, C+1):
            while ocean_fishing[i][j]:
                speed, direction, size = ocean_fishing[i][j].pop()
                x = i
                y = j
                dx = directionX[direction]
                dy = directionY[direction]
                for _ in range(speed):
                    if 0 < x+dx < R+1 and 0 < y+dy < C+1:
                        x += dx
                        y += dy
                    else:
                        if x+dx == 0:
                            direction = 2
                        elif x+dx == R+1:
                            direction = 1
                        elif y+dy == 0:
                            direction = 3
                        elif y+dy == C+1:
                            direction = 4
                        dx = directionX[direction]
                        dy = directionY[direction]
                        x += dx
                        y += dy
                ocean_move[x][y].append((speed, direction, size))

    for i in range(1, R+1):
        for j in range(1, C+1):
            if len(ocean_move[i][j]) > 1:
                maxSpeed, maxDirection, maxSize = ocean_move[i][j].pop()
                while ocean_move[i][j]:
                    speed, direction, size = ocean_move[i][j].pop()
                    if size > maxSize:
                        maxSpeed = speed
                        maxDirection = direction
                        maxSize = size
                ocean_fishing[i][j].append((maxSpeed, maxDirection, maxSize))
            elif len(ocean_move[i][j]) == 1:
                speed, direction, size = ocean_move[i][j].pop()
                ocean_fishing[i][j].append((speed, direction, size))

print(result)