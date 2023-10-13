import sys
import copy
from itertools import combinations

def infection():
    directionX = [1, 0, -1, 0]
    directionY = [0, 1, 0, -1]
    while test_virus:
        x, y = test_virus.pop()
        for i in range(4):
            dx = directionX[i]
            dy = directionY[i]
            if 0 <= x+dx < N and 0 <= y+dy < M and test_room[x+dx][y+dy] == 0:
                test_room[x+dx][y+dy] = 2
                test_virus.append((x+dx, y+dy))

N, M = map(int, sys.stdin.readline().rstrip().split())
room = []
for _ in range(N):
    room.append(list(map(int, sys.stdin.readline().rstrip().split())))

temp = []
virus = []
for i in range(N):
    for j in range(M):
        if room[i][j] == 0:
            temp.append((i, j))
        if room[i][j] == 2:
            virus.append((i, j))

result = 0
newLocation = list(combinations(temp, 3))
for location in newLocation:
    test_room = copy.deepcopy(room)
    test_virus = copy.deepcopy(virus)
    for t in location:
        test_room[t[0]][t[1]] = 1
    
    infection()
    count = 0
    for i in range(N):
        for j in range(M):
            if test_room[i][j] == 0:
                count += 1
    result = max(result, count)

print(result)