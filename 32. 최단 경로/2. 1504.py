import sys
import heapq

def bfs(endNode: int):
    while heap:
        dw, r = heapq.heappop(heap)

        if r == endNode:
            return

        for x in node[r]:
            w = x[0]
            v = x[1]
            if distance[v] > dw + w:
                distance[v] = dw + w
                heapq.heappush(heap, (distance[v], v))

V, E = map(int, sys.stdin.readline().rstrip().split())
heap = []
node = [[] for _ in range(V+1)]
distance = [800001] * (V+1)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    node[u].append((w, v))
    node[v].append((w, u))
N1, N2 = map(int, sys.stdin.readline().rstrip().split())

possibility = True
start = [1, N1, N2, 1, N2, N1]
end = [N1, N2, V, N2, N1, V]
temp1 = 0
temp2 = 0
for i in range(6):
    if i == 3:
        temp2 = temp1
        temp1 = 0

    heap = []
    distance = [800001] * (V+1)
    distance[start[i]] = 0
    heapq.heappush(heap, (0, start[i]))
    bfs(end[i])

    if distance[end[i]] == 800001:
        possibility = False
        break
    else:
        temp1 += distance[end[i]]

if possibility:
    if temp1 < temp2:
        print(temp1)
    else:
        print(temp2)
else:
    print(-1)