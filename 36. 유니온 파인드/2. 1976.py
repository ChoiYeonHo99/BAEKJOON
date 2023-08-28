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

N = int(sys.stdin.readline().rstrip())
union = []
for i in range(N+1):
    union.append(i)

M = int(sys.stdin.readline().rstrip())
for i in range(1, N+1):
    line = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, N+1):
        if line[j] == 1:
            combine(i, j)

trip = list(map(int, sys.stdin.readline().rstrip().split()))
temp = find(trip[0])
possibility = True
for i in range(1, len(trip)):
    if find(trip[i]) == temp:
        continue
    else:
        possibility = False
        break

if possibility:
    print("YES")
else:
    print("NO")