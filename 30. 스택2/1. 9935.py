import sys
from collections import deque

line = list(sys.stdin.readline().rstrip())
explosion = deque(list(sys.stdin.readline().rstrip()))
n = len(explosion)
result = deque([])
stack = deque([])

for i in range(len(line)):
    stack.append(line[i])
    if len(stack) == n:
        if stack == explosion:
            stack = deque([])
            while len(stack) < n - 1 and len(result) > 0:
                stack.appendleft(result.pop())
        else:
            result.append(stack.popleft())

result += stack
if len(result) == 0:
    print("FRULA")
else:
    print("".join(result))