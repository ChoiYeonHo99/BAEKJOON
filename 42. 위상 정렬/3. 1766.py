import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
degree = [0] * (N+1)
dic = {}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    degree[b] += 1
    dic.setdefault(a, [])
    dic[a].append(b)

heap = []
for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

result = []
for _ in range(N):
    node = heapq.heappop(heap)
    result.append(node)
    while node in dic and dic[node]:
        x = dic[node].pop()
        degree[x] -= 1
        if degree[x] == 0:
            heapq.heappush(heap, x)

print(*result)