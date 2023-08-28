import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque([i for i in range(1, n+1)])
size = n

while size > 1:
    queue.popleft()
    size -= 1
    front = queue[0]
    queue.popleft()
    queue.append(front)

print(queue[0])