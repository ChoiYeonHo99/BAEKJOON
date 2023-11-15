import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    visited = [False] * (N+1)
    parents = {}
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        parents[b] = a
    
    u, v = map(int, sys.stdin.readline().split())
    visited[u] = True
    while u in parents:
        u = parents[u]
        visited[u] = True
    
    while not visited[v]:
        v = parents[v]
    
    print(v)