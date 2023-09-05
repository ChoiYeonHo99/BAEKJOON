import sys
import heapq

def search():
    que = []
    heapq.heappush(que, (-world[0][0], 0, 0))

    visited = [[0] * n for _ in range(m)]
    visited[0][0] = 1

    while que:
        h, x, y = heapq.heappop(que)

        if x < m-1 and world[x][y] > world[x+1][y]:
            if visited[x+1][y] == 0:
                heapq.heappush(que, (-world[x+1][y], x+1, y))
            visited[x+1][y] += visited[x][y]
        if x > 0 and world[x][y] > world[x-1][y]:
            if visited[x-1][y] == 0:
                heapq.heappush(que, (-world[x-1][y], x-1, y))
            visited[x-1][y] += visited[x][y]
        if y < n-1 and world[x][y] > world[x][y+1]:
            if visited[x][y+1] == 0:
                heapq.heappush(que, (-world[x][y+1], x, y+1))
            visited[x][y+1] += visited[x][y]
        if y > 0 and world[x][y] > world[x][y-1]:
            if visited[x][y-1] == 0:
                heapq.heappush(que, (-world[x][y-1], x, y-1))
            visited[x][y-1] += visited[x][y]
    
    return visited[m-1][n-1]

world = []
m, n = map(int, sys.stdin.readline().rstrip().split())
for i in range(m):
    world.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(search())