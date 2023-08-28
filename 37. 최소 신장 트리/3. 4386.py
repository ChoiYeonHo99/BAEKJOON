import sys
import math

def distance(a: int, b: int):
    line1 = position[a][0] - position[b][0]
    line2 = position[a][1] - position[b][1]
    return math.sqrt((line1 * line1) + (line2 * line2))

def find(a: int):
    while a != union[a]:
        a = union[a]
    return a

def combine(a: int, b: int):
    x = find(a)
    y = find(b)
    if x != y:
        union[y] = x

n = int(sys.stdin.readline().rstrip())
union = [i for i in range(n+1)]
position = [[0] * 2 for _ in range(n+1)]
star = []
for i in range(1, n+1):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    position[i][0] = x
    position[i][1] = y
    for j in range(1, i):
        w = distance(i, j)
        star.append((w, i, j))

star.sort(reverse=True)
weight = 0
count = 0
while star:
    w, u, v = star.pop()
    if find(u) != find(v):
        combine(u, v)
        weight += w
        count += 1
    
    if count == n-1:
        break

print(round(weight, 2))