import sys
import heapq

MAX = 100001

def bfs(end: int):
    while heap:
        dw, r = heapq.heappop(heap)

        if r == end:
            return

        for i in range(3):
            w = 0
            v = 0
            if i == 0:
                w = 1
                v = r + 1
            if i == 1:
                w = 1
                v = r - 1
            if i == 2:
                w = 0
                v = r * 2

            if 0 <= v < MAX and distance[v] > dw + w :
                distance[v] = dw + w
                heapq.heappush(heap, (distance[v], v))

heap = []
distance = [MAX] * MAX
N, K = map(int, sys.stdin.readline().rstrip().split())
distance[N] = 0
heapq.heappush(heap, (0, N))
bfs(K)
print(distance[K])