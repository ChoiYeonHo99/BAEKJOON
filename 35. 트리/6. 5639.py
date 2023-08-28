import sys
from collections import deque

def divide(preOrder: deque):
    if not preOrder:
        return []

    root = preOrder.popleft()
    left = deque()
    right = deque()

    while preOrder:
        node = preOrder.popleft()
        if node > root:
            right.append(node)
        else:
            left.append(node)

    right = divide(right)
    left = divide(left)

    return list(left) + list(right) + [root]

preOrder = deque()
while 1:
    n = sys.stdin.readline().rstrip()
    if n == "":
        break
    preOrder.append(int(n))

sys.setrecursionlimit(10**9)
result = divide(preOrder)
for i in range(len(result)):
    print(result[i])