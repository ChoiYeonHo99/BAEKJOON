import sys

def find(a: int):
    if a == union[a]:
        return a
    else:
        union[a] = find(union[a])
    return union[a]

def combine(a: int, b: int):
    x = find(a)
    y = find(b)
    if x != y:
        union[y] = x

def check(a: int, b: int):
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")

n, m = map(int, sys.stdin.readline().rstrip().split())
union = []
for i in range(n+1):
    union.append(i)

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().rstrip().split())
    if c == 0:
        combine(a, b)
    elif c == 1:
        check(a, b)