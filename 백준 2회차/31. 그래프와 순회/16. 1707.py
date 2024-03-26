import sys

def dfs(r: int, myColor: int):
    global result
    if visited[r] == 0:
        visited[r] = myColor
    else:
        if visited[r] != myColor:
            result = False
        return

    yourColor = 0
    if myColor == 1:
        yourColor = 2
    else:
        yourColor = 1

    for x in node[r]:
        dfs(x, yourColor)

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    sys.setrecursionlimit(v * 10)
    node = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        node[a].append(b)
        node[b].append(a)

    visited = [0] * (v + 1)
    result = True
    for i in range(1, v+1):
        if visited[i] == 0:
            dfs(i, 1)
    if result:
        print("YES")
    else:
        print("NO")