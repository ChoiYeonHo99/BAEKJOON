import sys
from collections import deque

def rotation(num: int, direction: int, progress: int):
    if num == 0 or num == 5:
        return
    
    if progress == 0:
        if cogwheel[num][2] != cogwheel[num+1][6]:
            rotation(num+1, direction*-1, 1)
        if cogwheel[num][6] != cogwheel[num-1][2]:
            rotation(num-1, direction*-1, -1)
    elif progress == 1:
        if cogwheel[num][2] != cogwheel[num+1][6]:
            rotation(num+1, direction*-1, 1)
    elif progress == -1:
        if cogwheel[num][6] != cogwheel[num-1][2]:
            rotation(num-1, direction*-1, -1)

    if direction == 1:
        temp = cogwheel[num].pop()
        cogwheel[num].appendleft(temp)
    else:
        temp = cogwheel[num].popleft()
        cogwheel[num].append(temp)

t1 = sys.stdin.readline()
t2 = sys.stdin.readline()
t3 = sys.stdin.readline()
t4 = sys.stdin.readline()

cogwheel = [deque([1, 0, 1, 0, 1, 0, 1, 0]), deque(), deque(), deque(), deque(), deque([1, 0, 1, 0, 1, 0, 1, 0])]
for i in range(8):
    cogwheel[1].append(int(t1[i]))
    cogwheel[2].append(int(t2[i]))
    cogwheel[3].append(int(t3[i]))
    cogwheel[4].append(int(t4[i]))

K = int(sys.stdin.readline())
for _ in range(K):
    n, d = map(int, sys.stdin.readline().split())
    rotation(n, d, 0)

result = 0
if cogwheel[1][0] == 1:
    result += 1
if cogwheel[2][0] == 1:
    result += 2
if cogwheel[3][0] == 1:
    result += 4
if cogwheel[4][0] == 1:
    result += 8
print(result)