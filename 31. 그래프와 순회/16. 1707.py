import sys

def dfs(R: int, myColor: int):
    global result
    if visited[R] == 0:
        visited[R] = myColor
    else:
        if visited[R] != myColor:
            result = False
        return

    yourColor = 0
    if myColor == 1:
        yourColor = 2
    else:
        yourColor = 1

    for x in node[R]:
        dfs(x, yourColor)

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    sys.setrecursionlimit(V * 10)
    node = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        node[u].append(v)
        node[v].append(u)

    result = True
    for i in range(1, V+1):
        if visited[i] == 0:
            dfs(i, 1)
    if result:
        print("YES")
    else:
        print("NO")