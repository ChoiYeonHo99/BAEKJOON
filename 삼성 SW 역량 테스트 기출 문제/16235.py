import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
winter = [[0] * (N+1)]
for i in range(N):
    winter.append([0] + list(map(int, sys.stdin.readline().split())))

nutriment = [[5] * (N+1) for _ in range(N+1)]
tree = [[deque() for _ in range(N+1)] for _ in range(N+1)]
summer = []
directionX = [1, 0, -1, 0, 1, 1, -1, -1]
directionY = [0, 1, 0, -1, 1, -1, -1, 1]
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x][y].append(z)

for _ in range(K):
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(len(tree[i][j])):
                if nutriment[i][j] < tree[i][j][k]:
                    for _ in range(k, len(tree[i][j])):
                        summer.append((tree[i][j].pop(), i, j))
                    break
                else:
                    nutriment[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

    while summer:
        z, x, y = summer.pop()
        nutriment[x][y] += z // 2

    for x in range(1, N+1):
        for y in range(1, N+1):
            for k in range(len(tree[x][y])):
                if tree[x][y][k] % 5 == 0:
                    for i in range(8):
                        dx = directionX[i]
                        dy = directionY[i]
                        if 1 <= x+dx <= N and 1 <= y+dy <= N:
                            tree[x+dx][y+dy].appendleft(1)

    for i in range(1, N+1):
        for j in range(1, N+1):
            nutriment[i][j] += winter[i][j]

result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        result += len(tree[i][j])
print(result)