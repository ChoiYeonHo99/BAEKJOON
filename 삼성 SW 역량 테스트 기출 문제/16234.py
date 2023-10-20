import sys
from collections import deque

def search(a: int, b: int, num: int):
    q = deque()
    q.append((a, b))
    occur = False
    while q:
        x, y = q.popleft()

        for i in range(4):
            dx = directionX[i]
            dy = directionY[i]

            if 0 <= x + dx < N and 0 <= y + dy < N and union[x+dx][y+dy] == 0 and L <= abs(world[x+dx][y+dy] - world[x][y]) <= R:
                union[x][y] = num
                union[x+dx][y+dy] = num
                q.append((x+dx, y+dy))
                occur = True

    return occur

N, L, R = map(int, sys.stdin.readline().split())
world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))

directionX = [1, 0, -1, 0]
directionY = [0, 1, 0, -1]

end = True
count = 0
while end:
    union = [[0] * N for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(N):
            if union[i][j] == 0:
                if search(i, j, num):
                    num += 1

    member = [[0] * 2 for _ in range(num+1)]
    for i in range(N):
        for j in range(N):
            member[union[i][j]][0] += world[i][j]
            member[union[i][j]][1] += 1

    if member[0][1] == N**2:
        end = False
        print(count)

    count += 1
    for i in range(N):
        for j in range(N):
            if union[i][j] != 0:
                world[i][j] = member[union[i][j]][0] // member[union[i][j]][1]