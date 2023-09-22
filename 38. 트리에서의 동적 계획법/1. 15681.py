import sys

def setParents(n: int):
    visited[n] = True
    for x in node[n]:
        if visited[x] == False:
            parents[x] = n
            childs[n].append(x)
            setParents(x)

def findChilds(n: int):
    result = 1
    for x in childs[n]:
        result += findChilds(x)
    
    count[n] = result
    return result

N, R, Q = map(int, sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(N * 10)
node = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().rstrip().split())
    node[U].append(V)
    node[V].append(U)

visited = [False] * (N+1)
parents = {}
parents[R] = 0
childs = [[] for _ in range(N+1)]
count = {}
setParents(R)
findChilds(R)
for _ in range(Q):
    i = int(sys.stdin.readline().rstrip())
    print(count[i])