import sys
from collections import deque

def rotation(d: int):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    if d == 4:
        return 3

N, K = map(int, sys.stdin.readline().split())
color = [[-1] * (N+1)]
for _ in range(N):
    color.append([-1] + list(map(int, sys.stdin.readline().split())))

directionX = [0, 0, 0, -1, 1]
directionY = [0, 1, -1, 0, 0]
field = [[deque() for _ in range(N+1)] for _ in range(N+1)]
horse = [[0, 0, 0] for _ in range(K+1)]
for i in range(1, K+1):
    x, y, d = map(int, sys.stdin.readline().split())
    field[x][y].append(i)
    horse[i][0] = x
    horse[i][1] = y
    horse[i][2] = d

possible = False
for T in range(1, 1001):
    for i in range(1, K+1):
        x = horse[i][0]
        y = horse[i][1]
        d = horse[i][2]
        dx = directionX[d]
        dy = directionY[d]
        nx = x
        ny = y

        if len(field[x][y]) >= 4:
            print(T)
            possible = True
            break

        reverse = False
        if 0 < x+dx <= N and 0 < y+dy <= N:
            if color[x+dx][y+dy] == 2:
                d = rotation(d)
                dx = directionX[d]
                dy = directionY[d]
                if 0 < x+dx <= N and 0 < y+dy <= N and color[x+dx][y+dy] != 2:
                    if color[x+dx][y+dy] == 1:
                        reverse = True
                    nx = x + dx
                    ny = y + dy
                horse[i][2] = d

            else:
                if color[x+dx][y+dy] == 1:
                    reverse = True
                nx = x + dx
                ny = y + dy

        else:
            d = rotation(d)
            dx = directionX[d]
            dy = directionY[d]
            if color[x+dx][y+dy] != 2:
                if color[x+dx][y+dy] == 1:
                    reverse = True
                nx = x + dx
                ny = y + dy
            horse[i][2] = d

        temp = deque()
        while field[x][y]:
            n = field[x][y].pop()
            if reverse:
                temp.append(n)
            else:
                temp.appendleft(n)

            if n == i:
                break

        while temp:
            n = temp.popleft()
            horse[n][0] = nx
            horse[n][1] = ny
            field[nx][ny].append(n)

        if len(field[nx][ny]) >= 4:
            print(T)
            possible = True
            break

    if possible:
        break

if not possible:
    print(-1)