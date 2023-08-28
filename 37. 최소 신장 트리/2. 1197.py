import sys

def find(a: int):
    while a != union[a]:
        a = union[a]
    return a

def combine(a: int, b: int):
    x = find(a)
    y = find(b)
    if x != y:
        union[y] = x

V, E = map(int, sys.stdin.readline().rstrip().split())
union = [i for i in range(V+1)]
distance = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    distance.append((C, A, B))

distance.sort(reverse=True)
weight = 0
count = 0
while distance:
    w, u, v = distance.pop()
    if find(u) != find(v):
        combine(u, v)
        weight += w
        count += 1
    
    if count == V-1:
        break

print(weight)