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

m, n = map(int, sys.stdin.readline().rstrip().split())
while 1:
    if m == 0 and n == 0:
        break

    union = [i for i in range(m)]
    distance = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        distance.append((z, x, y))
        total += z

    distance.sort(reverse=True)
    weight = 0
    count = 0
    while distance:
        c, a, b = distance.pop()
        if find(a) != find(b):
            combine(a, b)
            weight += c
            count += 1
        
        if count == m-1:
            break

    m, n = map(int, sys.stdin.readline().rstrip().split())
    print(total - weight)