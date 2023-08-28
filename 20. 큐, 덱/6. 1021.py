import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
index_list = list(map(int, sys.stdin.readline().rstrip().split()))
queue = deque([i for i in range(1, n+1)])
count = 0

def pop():
    queue.popleft()

def moveLeft():
    front = queue[0]
    queue.popleft()
    queue.append(front)

def moveRight():
    back = queue[len(queue)-1]
    queue.pop()
    queue.appendleft(back)

for i in index_list:
    index = queue.index(i)
    if index == 0:
        pop()
    elif index >= len(queue) / 2:
        for _ in range(len(queue) - (index)):
            moveRight()
            count += 1
        pop()
    else:
        for _ in range(index):
            moveLeft()
            count += 1
        pop()

print(count)