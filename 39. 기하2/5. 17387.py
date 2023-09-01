import sys

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    return (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)
    
x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().rstrip().split())

c1 = ccw(x1, y1, x2, y2, x3, y3)
c2 = ccw(x1, y1, x2, y2, x4, y4)
c3 = ccw(x3, y3, x4, y4, x1, y1)
c4 = ccw(x3, y3, x4, y4, x2, y2)

if c1 == c2 == c3 == c4 == 0:
    if x1 >= min(x3, x4) and x1 <= max(x3, x4) and y1 >= min(y3, y4) and y1 <= max(y3, y4):
        print(1)
    elif x2 >= min(x3, x4) and x2 <= max(x3, x4) and y2 >= min(y3, y4) and y2 <= max(y3, y4):
        print(1)
    elif x3 >= min(x1, x2) and x3 <= max(x1, x2) and y3 >= min(y1, y2) and y3 <= max(y1, y2):
        print(1)
    elif x4 >= min(x1, x2) and x4 <= max(x1, x2) and y4 >= min(y1, y2) and y4 <= max(y1, y2):
        print(1)
    else:
        print(0)
elif c1 * c2 <= 0 and c3 * c4 <= 0:
    print(1)
else:
    print(0)