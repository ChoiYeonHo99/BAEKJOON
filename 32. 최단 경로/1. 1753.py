import sys
import heapq

def bfs():
    while heap:
        dw, r = heapq.heappop(heap)

        for x in node[r]:
            w = x[0]
            v = x[1]
            if distance[v] > dw + w:
                distance[v] = dw + w
                heapq.heappush(heap, (distance[v], v))

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())
heap = []
node = [[] for _ in range(V+1)]
distance = [200001] * (V+1)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    node[u].append((w, v))

distance[K] = 0
heapq.heappush(heap, (0, K))
bfs()

for i in range(1, V+1):
    if distance[i] == 200001:
        print("INF")
    else:
        print(distance[i])