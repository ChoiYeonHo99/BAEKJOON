import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, index = map(int, sys.stdin.readline().rstrip().split())
    queue = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    count = 0
    while len(queue) > 0:
        importance = queue[0]
        printable = True
        for i in range(len(queue)):
            if importance < queue[i]:
                front = queue[0]
                queue.popleft()
                queue.append(front)
                printable = False
                if index == 0:
                    index = len(queue) - 1
                else:
                    index -= 1
                break
        if printable:
            queue.popleft()
            count += 1
            if index == 0:
                break
            else:
                index -= 1
    print(count)