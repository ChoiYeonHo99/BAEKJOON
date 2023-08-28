import sys

def preOrder(r: int):
    if r == -19:
        return
    result.append(r)
    preOrder(node[r][0])
    preOrder(node[r][1])

def inOrder(r: int):
    if r == -19:
        return
    inOrder(node[r][0])
    result.append(r)
    inOrder(node[r][1])

def postOrder(r: int):
    if r == -19:
        return
    postOrder(node[r][0])
    postOrder(node[r][1])
    result.append(r)

N = int(sys.stdin.readline().rstrip())
node = [[0] * 2 for _ in range(N)]
for _ in range(N):
    A, B, C = sys.stdin.readline().rstrip().split()
    a = ord(A) - 65
    b = ord(B) - 65
    c = ord(C) - 65
    node[a][0] = b
    node[a][1] = c

result = []
preOrder(0)
for i in range(N):
    print(chr(result[i]+65), end = "")
print()

result.clear()
inOrder(0)
for i in range(N):
    print(chr(result[i]+65), end = "")
print()

result.clear()
postOrder(0)
for i in range(N):
    print(chr(result[i]+65), end = "")