import sys
from collections import deque

def searchIsland(a: int, b: int):
    visited[a][b] = True
    que = deque()
    que.append((a, b))
    result = []

    while que:
        x, y = que.popleft()
        result.append((x, y))

        if x < N-1 and not visited[x+1][y] and island[x+1][y] == 1:
            que.append((x+1, y))
            visited[x+1][y] = True
        if x > 0 and not visited[x-1][y] and island[x-1][y] == 1:
            que.append((x-1, y))
            visited[x-1][y] = True
        if y < M-1 and not visited[x][y+1] and island[x][y+1] == 1:
            que.append((x, y+1))
            visited[x][y+1] = True
        if y > 0 and not visited[x][y-1] and island[x][y-1] == 1:
            que.append((x, y-1))
            visited[x][y-1] = True
    
    return result

def searchDistance(u: int, v: int):
    if u == v:
        return

    minValue = 1000
    for x1, y1 in unionIsland[u]:
        for x2, y2 in unionIsland[v]:
            d = 0
            if x1 == x2 and isPossibleBridge(True, y1, y2, x1):
                d = abs(y1 - y2) - 1
            if y1 == y2 and isPossibleBridge(False, x1, x2, y1):
                d = abs(x1 - x2) - 1

            if d >= 2 and d < minValue:
                minValue = d

    if minValue != 1000:
        distance.append((minValue, u, v))

def isPossibleBridge(type: bool, a: int, b: int, xy: int):
    if type:
        if a < b:
            for i in range(a+1, b):
                if island[xy][i] == 1:
                    return False
        else:
            for i in range(b+1, a):
                if island[xy][i] == 1:
                    return False
    else:
        if a < b:
            for i in range(a+1, b):
                if island[i][xy] == 1:
                    return False
        else:
            for i in range(b+1, a):
                if island[i][xy] == 1:
                    return False
    return True

def find(a: int):
    while a != union[a]:
        a = union[a]
    return a

def combine(a: int, b: int):
    x = find(a)
    y = find(b)
    if x != y:
        union[y] = x

N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [[False] * M for _ in range(N)]
island = []
unionIsland = []
distance = []
countIsland = 0
for _ in range(N):
    island.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and not visited[i][j]:
            unionIsland.append(searchIsland(i, j))
            countIsland += 1

for i in range(countIsland):
    for j in range(i+1, countIsland):
        searchDistance(i, j)

distance.sort(reverse=True)
union = [i for i in range(countIsland)]
weight = 0
count = 0
while distance:
    w, u, v = distance.pop()

    if find(u) != find(v):
        combine(u, v)
        weight += w
        count += 1
    
    if count == countIsland - 1:
        break

if count == countIsland - 1:
    print(weight)
else:
    print(-1)