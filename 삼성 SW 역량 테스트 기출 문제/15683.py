import sys
import copy

def observe():
    global result, room, cctv
    if not cctv:
        count = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    count += 1
        result = min(result, count)
        return

    num, x, y = cctv.pop()
    temp = copy.deepcopy(room)
    if num == 1:
        for i in range(4):
            dx = direction1X[i]
            dy = direction1Y[i]
            while 0 <= x + dx < N and 0 <= y + dy < M:
                if room[x+dx][y+dy] != 6:
                    if room[x+dx][y+dy] == 0:
                        room[x+dx][y+dy] = -1
                else:
                    break
                dx += direction1X[i]
                dy += direction1Y[i]
            observe()
            room = copy.deepcopy(temp)

    if num == 2:
        for i in range(0, 4, 2):
            for j in range(2):
                dx = direction2X[i+j]
                dy = direction2Y[i+j]
                while 0 <= x + dx < N and 0 <= y + dy < M:
                    if room[x+dx][y+dy] != 6:
                        if room[x+dx][y+dy] == 0:
                            room[x+dx][y+dy] = -1
                    else:
                        break
                    dx += direction2X[i+j]
                    dy += direction2Y[i+j]
            observe()
            room = copy.deepcopy(temp)

    if num == 3:
        for i in range(0, 8, 2):
            for j in range(2):
                dx = direction3X[i+j]
                dy = direction3Y[i+j]
                while 0 <= x + dx < N and 0 <= y + dy < M:
                    if room[x+dx][y+dy] != 6:
                        if room[x+dx][y+dy] == 0:
                            room[x+dx][y+dy] = -1
                    else:
                        break
                    dx += direction3X[i+j]
                    dy += direction3Y[i+j]
            observe()
            room = copy.deepcopy(temp)

    if num == 4:
        for i in range(0, 12, 3):
            for j in range(3):
                dx = direction4X[i+j]
                dy = direction4Y[i+j]
                while 0 <= x + dx < N and 0 <= y + dy < M:
                    if room[x+dx][y+dy] != 6:
                        if room[x+dx][y+dy] == 0:
                            room[x+dx][y+dy] = -1
                    else:
                        break
                    dx += direction4X[i+j]
                    dy += direction4Y[i+j]
            observe()
            room = copy.deepcopy(temp)

    if num == 5:
        for i in range(4):
            dx = direction1X[i]
            dy = direction1Y[i]
            while 0 <= x + dx < N and 0 <= y + dy < M:
                if room[x+dx][y+dy] != 6:
                    if room[x+dx][y+dy] == 0:
                        room[x+dx][y+dy] = -1
                else:
                    break
                dx += direction1X[i]
                dy += direction1Y[i]
        observe()
        room = copy.deepcopy(temp)
    
    cctv.append((num, x, y))

N, M = map(int, sys.stdin.readline().split())
direction1X = [1, 0, -1, 0]
direction1Y = [0, 1, 0, -1]
direction2X = [1, -1, 0, 0]
direction2Y = [0, 0, 1, -1]
direction3X = [1, 0, -1, 0, 0, -1, 0, 1]
direction3Y = [0, 1, 0, -1, 1, 0, -1, 0]
direction4X = [-1, 0, 0, 0, -1, 1, 1, 0, 0, 0, 1, -1]
direction4Y = [0, 1, -1, 1, 0, 0, 0, 1, -1, -1, 0, 0]
room = []
cctv = []
for i in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if 0 < room[i][j] < 6:
            cctv.append((room[i][j], i, j))

result = N * M
observe()
print(result)