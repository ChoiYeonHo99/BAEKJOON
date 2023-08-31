import sys

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    comp = (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)

    if comp > 0:
        return 1
    else:
        return -1

x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().rstrip().split())

if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) < 0:
    print(1)
else:
    print(0)