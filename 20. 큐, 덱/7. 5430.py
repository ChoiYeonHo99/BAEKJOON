import sys
from collections import deque

queue = deque([])
global reverse
reverse = False

def R():
    global reverse
    reverse = not reverse

def D():
    if len(queue) == 0:
        return True
    if reverse:
        queue.pop()
    else:
        queue.popleft()
    return False

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    n_list = list(sys.stdin.readline().rstrip().strip('['']').split(','))
    if n == 0:
        queue = deque([])
    else:
        queue = deque(list(map(int, n_list)))

    reverse = False
    error = False
    for i in range(len(command)):
        if command[i] == "R":
            R()
        else:
            error = D()
            if error:
                print("error")
                break
    if error:
        continue
    else:
        if reverse:
            queue.reverse()
        print("[" + ','.join(map(str, queue)) + "]")