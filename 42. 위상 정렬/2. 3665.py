import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    degree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]

    lastYear = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        for j in range(i+1, N):
            graph[lastYear[i]].append(lastYear[j])
            degree[lastYear[j]] += 1

    M = int(sys.stdin.readline())
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        temp = True

        for i in graph[a]:
            if i == b:
                graph[a].remove(b)
                degree[b] -= 1
                graph[b].append(a)
                degree[a] += 1
                temp = False

        if temp:
            graph[b].remove(a)
            degree[a] -= 1
            graph[a].append(b)
            degree[b] += 1

    q = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)

    if not q:
        print("IMPOSSIBLE")
        continue

    result = []
    while q:
        if len(q) > 1:
            break

        node = q.popleft()
        result.append(node)
        for i in graph[node]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
            if degree[i] < 0:
                break

    if len(result) != N:
        print("IMPOSSIBLE")
    else:
        print(*result)