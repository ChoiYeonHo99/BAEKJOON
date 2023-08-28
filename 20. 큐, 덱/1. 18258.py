import sys
from collections import deque

queue = deque([])
n = int(sys.stdin.readline().rstrip())
size = 0

for i in range(n):
    s = sys.stdin.readline().rstrip().split()
    if s[0] == "push":
        queue.append(int(s[1]))
        size += 1
    elif s[0] == "pop":
        if size == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
            size -= 1
    elif s[0] == "size":
        print(size)
    elif s[0] == "empty":
        if size == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if size == 0:
            print(-1)
        else:
            print(queue[0])
    elif s[0] == "back":
        if size == 0:
            print(-1)
        else:
            print(queue[size-1])