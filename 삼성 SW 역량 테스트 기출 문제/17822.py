import sys
import copy

def rotation(n: int, d: int, k: int):
    temp = copy.deepcopy(circle[n])
    if d == 0:
        for i in range(M):
            circle[n][i] = temp[(i - k + M) % M]
    else:
        for i in range(M):
            circle[n][i] = temp[(i + k) % M]

def remove(x: int, y: int, a: int):
    circle[x][y] = 0
    for i in range(4):
        dx = directionX[i]
        dy = directionY[i]
        if 0 < x+dx <= N and 0 <= y+dy < M and a == circle[x+dx][y+dy]:
            remove(x+dx, y+dy, a)

    if y == 0 and a == circle[x][M-1]:
        remove(x, M-1, a)
    if y == M-1 and a == circle[x][0]:
        remove(x, 0, a)

def search(x: int, y: int):
    for i in range(4):
        dx = directionX[i]
        dy =directionY[i]
        if 0 < x+dx <= N and 0 <= y+dy < M and circle[x][y] == circle[x+dx][y+dy]:
            return True

    if y == 0 and circle[x][0] == circle[x][M-1]:
        return True
    if y == M-1 and circle[x][0] == circle[x][M-1]:
        return True

    return False

N, M, T = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(N * M * 10)
circle = [[0] * M]
directionX = [1, 0, -1, 0]
directionY = [0, 1, 0, -1]
for _ in range(N):
    circle.append(list(map(int, sys.stdin.readline().split())))

for _ in range(T):
    x, d, k = map(int, sys.stdin.readline().split())
    for i in range(x, N+1, x):
        rotation(i, d, k)

    case2 = True
    for i in range(1, N+1):
        for j in range(M):
            if circle[i][j] != 0 and search(i, j):
                case2 = False
                remove(i, j, circle[i][j])

    if case2:
        count = 0
        val = 0
        for i in range(1, N+1):
            for j in range(M):
                if circle[i][j] != 0:
                    count += 1
                    val += circle[i][j]

        if count != 0:
            val /= count
            for i in range(1, N+1):
                for j in range(M):
                    if circle[i][j] == 0:
                        continue

                    if circle[i][j] < val:
                        circle[i][j] += 1
                    elif circle[i][j] > val:
                        circle[i][j] -= 1

result = 0
for i in range(1, N+1):
    result += sum(circle[i])

print(result)