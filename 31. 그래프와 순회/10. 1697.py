import sys
from collections import deque

def bfs(n, k):
    queue = deque([(n, 0)])
    visited[n] = True

    while queue:
        x, count = queue.popleft()

        if x == k:
            return count

        for i in range(3):
            nx = 0
            if i == 0:
                nx = x + 1
            if i == 1:
                nx = x - 1
            if i == 2:
                nx = x * 2

            if nx >= 0 and nx < 100001 and visited[nx] == False:
                queue.append((nx, count + 1))
                visited[nx] = True

n, k = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * 100001

answer = bfs(n, k)
print(answer)