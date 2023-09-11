import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline().rstrip())
node = [[] for _ in range(n+1)]
dp = [100000000] * (n+1)
m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    a, b, d = map(int, sys.stdin.readline().rstrip().split())
    node[a].append((d, b))
for i in range(n):
    node[i].sort()
s, e = map(int, sys.stdin.readline().rstrip().split())
dp[s] = 0

q = [(0, s, [s])]
while q:
    distance, u, path = heappop(q)

    if u == e:
        print(distance)
        print(len(path))
        print(*path)
        break

    for r, v in node[u]:
        if distance + r < dp[v]:
            dp[v] = distance + r
            heappush(q, (distance + r, v, path + [v]))