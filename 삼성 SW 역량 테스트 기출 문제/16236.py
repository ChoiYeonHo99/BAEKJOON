import sys
from collections import deque

def search():
    global time, x, y
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * N  for _ in range(N)]
    visited[x][y] = True
    possibleFish = []
    minDistance = N**2

    while q:
        a, b, d = q.popleft()
        if d >= minDistance:
            break

        for i in range(4):
            dx = directionX[i]
            dy = directionY[i]
            if 0 <= a+dx < N and 0 <= b+dy < N and ocean[a+dx][b+dy] <= level and not visited[a+dx][b+dy]:
                if ocean[a+dx][b+dy] != 0 and ocean[a+dx][b+dy] < level:
                    possibleFish.append((a+dx, b+dy))
                    visited[a+dx][b+dy] = True
                    minDistance = d+1
                else:
                    q.append((a+dx, b+dy, d+1))
                    visited[a+dx][b+dy] = True
    
    if len(possibleFish) == 0:
        return False

    minX = N
    minY = N
    targetX = 0
    targetY = 0
    while possibleFish:
        a, b = possibleFish.pop()
        if a < minX:
            minX = a
            minY = b
            targetX = a
            targetY = b
        elif a == minX:
            if b < minY:
                minX = a
                minY = b
                targetX = a
                targetY = b
    
    ocean[x][y] = 0
    ocean[targetX][targetY] = 9
    time += minDistance
    x = targetX
    y = targetY

    return True



N = int(sys.stdin.readline())
ocean = []
x = 0
y = 0
level = 2
meal = 0
time = 0
directionX = [1, 0, -1, 0]
directionY = [0, 1, 0, -1]
for i in range(N):
    ocean.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if ocean[i][j] == 9:
            x = i
            y = j

while True:
    if search():
        meal += 1
        if meal == level:
            meal = 0
            level += 1
    else:
        break

print(time)