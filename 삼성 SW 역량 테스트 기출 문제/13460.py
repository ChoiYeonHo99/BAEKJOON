import sys
from collections import deque
import copy

def tilt(rx, ry, bx, by, state, count, d):
    temp = [rx, ry, bx, by]
    if count >= 10:
        return 2

    goal_red = False
    goal_blue = False
    if d == "left":
        if rx > bx:
            while state[by][bx-1] == True:
                state[by][bx] = True
                bx -= 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
            while state[ry][rx-1] == True:
                state[ry][rx] = True
                rx -= 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
        else:
            while state[ry][rx-1] == True:
                state[ry][rx] = True
                rx -= 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
            while state[by][bx-1] == True:
                state[by][bx] = True
                bx -= 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
    elif d == "right":
        if rx < bx:
            while state[by][bx+1] == True:
                state[by][bx] = True
                bx += 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
            while state[ry][rx+1] == True:
                state[ry][rx] = True
                rx += 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
        else:
            while state[ry][rx+1] == True:
                state[ry][rx] = True
                rx += 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
            while state[by][bx+1] == True:
                state[by][bx] = True
                bx += 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
    elif d == "up":
        if ry < by:
            while state[ry-1][rx] == True:
                state[ry][rx] = True
                ry -= 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
            while state[by-1][bx] == True:
                state[by][bx] = True
                by -= 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
        else:
            while state[by-1][bx] == True:
                state[by][bx] = True
                by -= 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
            while state[ry-1][rx] == True:
                state[ry][rx] = True
                ry -= 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
    elif d == "down":
        if ry > by:
            while state[ry+1][rx] == True:
                state[ry][rx] = True
                ry += 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False
            while state[by+1][bx] == True:
                state[by][bx] = True
                by += 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
        else:
            while state[by+1][bx] == True:
                state[by][bx] = True
                by += 1
                if bx == Ox and by == Oy:
                    goal_blue = True
                    break
                state[by][bx] = False
            while state[ry+1][rx] == True:
                state[ry][rx] = True
                ry += 1
                if rx == Ox and ry == Oy:
                    goal_red = True
                    break
                state[ry][rx] = False

    if goal_blue == True:
        return 0
    if goal_red == True:
        return 1
    if temp == [rx, ry, bx, by]:
        return 2

    q.append((rx, ry, bx, by, state, count+1))
    return 2

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [[False] * M for _ in range(N)]
direction = ["left", "right", "up", "down"]
Rx, Ry, Bx, By, Ox, Oy = 0, 0, 0, 0, 0, 0
for i in range(N):
    line = sys.stdin.readline().rstrip()
    for j in range(M):
        if line[j] == "#":
            board[i][j] = False
        elif line[j] == ".":
            board[i][j] = True
        elif line[j] == "R":
            board[i][j] = False
            Rx = j
            Ry = i
        elif line[j] == "B":
            board[i][j] = False
            Bx = j
            By = i
        elif line[j] == "O":
            board[i][j] = True
            Ox = j
            Oy = i

q = deque()
q.append((Rx, Ry, Bx, By, board, 0))
possible = False
while q:
    rx, ry, bx, by, world, count = q.popleft()
    for d in direction:
        temp = copy.deepcopy(world)
        result = tilt(rx, ry, bx, by, temp, count, d)
        if result == 1:
            print(count+1)
            possible = True
            q = deque()
            break

if possible == False:
    print(-1)