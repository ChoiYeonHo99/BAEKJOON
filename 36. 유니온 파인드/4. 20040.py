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

n, m = map(int, sys.stdin.readline().rstrip().split())
union = [i for i in range(n)]

turn = 0
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if find(a) == find(b):
        turn = i
        break
    combine(a, b)

print(turn)