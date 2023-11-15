import sys
from itertools import combinations
from collections import deque
import copy

def infection(x: int, y: int, t: int):
    directionX = [1, 0, -1, 0]
    directionY = [0, 1, 0, -1]

    for i in range(4):
        dx = directionX[i]
        dy = directionY[i]
        if 0 <= x+dx < N and 0 <= y+dy <N and not visited[x+dx][y+dy]:
            if test_laboratory[x+dx][y+dy] == 0:
                test_laboratory[x+dx][y+dy] = 2
                q.append((x+dx, y+dy, t+1))
                visited[x+dx][y+dy] = True
            elif test_laboratory[x+dx][y+dy] == 2:
                possible = True
                for a in range(N):
                    for b in range(N):
                        if test_laboratory[a][b] == 0:
                            possible = False
                            break
                    if possible == False:
                        break
                
                if possible:
                    return
                else:
                    q.append((x+dx, y+dy, t+1))
                    visited[x+dx][y+dy] = True

N, M = map(int, sys.stdin.readline().split())
laboratory = []
virus = []
for i in range(N):
    laboratory.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if laboratory[i][j] == 2:
            virus.append((i, j))

comb_virus = list(combinations(virus, M))

result = N**2
for test_virus in comb_virus:
    test_laboratory = copy.deepcopy(laboratory)
    visited = [[False] * N for _ in range(N)]
    q = deque()
    for x in test_virus:
        q.append((x[0], x[1], 0))
        visited[x[0]][x[1]] = True

    maxValue = 0
    while q:
        x, y, t = q.popleft()
        maxValue = t
        infection(x, y, t)

    possible = True
    for i in range(N):
        for j in range(N):
            if test_laboratory[i][j] == 0:
                possible = False
                break
        if possible == False:
            break
    
    if possible:
        result = min(result, maxValue)

if result == N**2:
    print(-1)
else:
    print(result)