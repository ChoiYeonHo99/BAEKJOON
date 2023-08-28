import sys

def find(a: str):
    if a == union[a]:
        return a
    else:
        union[a] = find(union[a])
    return union[a]

def combine(a: str, b: str):
    x = find(a)
    y = find(b)
    if x != y:
        union[y] = x
        freind[x] += freind[y]

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    F = int(sys.stdin.readline().rstrip())

    union = {}
    freind = {}

    for _ in range(F):
        a, b = sys.stdin.readline().rstrip().split()

        if not a in union:
            union[a] = a
            freind[a] = 1
        if not b in union:
            union[b] = b
            freind[b] = 1

        combine(union[a], union[b])
        print(freind[find(a)])