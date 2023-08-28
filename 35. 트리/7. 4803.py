import sys
from collections import deque

def search(r: int):
    que = deque([r])
    parent = {}
    parent[r] = 0
    visited[r] = True

    while que:
        u = que.popleft()
        
        for v in node[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                que.append(v)
            else:
                if parent[u] != v:
                    return False
    return True

test = 0
while 1:
    n, m = map(int, sys.stdin.readline().rstrip().split())

    if n == 0 and m == 0:
        break

    count = 0
    test += 1
    node = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    visited[0] = True

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        node[u].append(v)
        node[v].append(u)

    for i in range(1, n+1):
        if visited[i] == False:
            if search(i):
                count += 1

    if count == 0:
        print("Case " + str(test) + ": No trees.")
    elif count == 1:
        print("Case " + str(test) + ": There is one tree.")
    else:
        print("Case " + str(test) + ": A forest of " + str(count) + " trees.")