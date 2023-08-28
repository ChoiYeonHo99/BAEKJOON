import sys
import heapq

MAX = 2000001

def bfs(end: int):
    while heap:
        dw, r = heapq.heappop(heap)

        if r == end:
            return

        for x in node[r]:
            w = x[0]
            v = x[1]
            if distance[v] > dw + w:
                distance[v] = dw + w
                heapq.heappush(heap, (distance[v], v))

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split())
    node = [[] for _ in range(n+1)]
    result = []

    s, g, h = map(int, sys.stdin.readline().rstrip().split())

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        node[a].append((d, b))
        node[b].append((d, a))

    for _ in range(t):
        x = int(sys.stdin.readline().rstrip())

        possibility = True
        start_nodes = [s, g, h, s, h, g]
        end_nodes = [g, h, x, h, g, x]
        temp1 = 0
        temp2 = 0

        for i in range(6):
            heap = []
            distance = [MAX] * (n+1)
            distance[start_nodes[i]] = 0
            heapq.heappush(heap, (0, start_nodes[i]))
            bfs(end_nodes[i])

            if distance[end_nodes[i]] == MAX:
                possibility = False
                break

            if i <= 2:
                temp1 += distance[end_nodes[i]]
            else:
                temp2 += distance[end_nodes[i]]

        heap = []
        distance = [MAX] * (n+1)
        distance[s] = 0
        heapq.heappush(heap, (0, s))
        bfs(x)

        if possibility and (distance[x] == temp1 or distance[x] == temp2):
            result.append(x)

    result.sort()
    print(*result)