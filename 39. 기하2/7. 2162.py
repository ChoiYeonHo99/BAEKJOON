import sys

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    return (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)

def check(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int):
    c1 = ccw(x1, y1, x2, y2, x3, y3)
    c2 = ccw(x1, y1, x2, y2, x4, y4)
    c3 = ccw(x3, y3, x4, y4, x1, y1)
    c4 = ccw(x3, y3, x4, y4, x2, y2)

    if c1 == c2 == c3 == c4 == 0:
        if x1 >= min(x3, x4) and x1 <= max(x3, x4) and y1 >= min(y3, y4) and y1 <= max(y3, y4):
            return True
        elif x2 >= min(x3, x4) and x2 <= max(x3, x4) and y2 >= min(y3, y4) and y2 <= max(y3, y4):
            return True
        elif x3 >= min(x1, x2) and x3 <= max(x1, x2) and y3 >= min(y1, y2) and y3 <= max(y1, y2):
            return True
        elif x4 >= min(x1, x2) and x4 <= max(x1, x2) and y4 >= min(y1, y2) and y4 <= max(y1, y2):
            return True
        else:
            return False
    elif c1 * c2 <= 0 and c3 * c4 <= 0:
        return True
    else:
        return False

n = int(sys.stdin.readline().rstrip())
position = []
for _ in range(n):
    position.append(list(map(int, sys.stdin.readline().rstrip().split())))

group = [[] for _ in range(n)]
group[0].append(position[0])
index = 0
count = 1
for i in range(1, n):
    possible = False
    for j in range(count):
        for k in range(len(group[j])):
            if check(position[i][0], position[i][1], position[i][2], position[i][3], group[j][k][0], group[j][k][1], group[j][k][2], group[j][k][3]):
                if possible:
                    for x in group[j]:
                        group[index].append(x)
                    group[j].clear()
                else:
                    group[j].append(position[i])
                    index = j
                    possible = True
                break
    if not possible:
        group[count].append(position[i])
        count += 1

maxValue = 0
groupCount = 0
for i in range(len(group)):
    if maxValue < len(group[i]):
        maxValue = len(group[i])
    if len(group[i]) != 0:
        groupCount += 1

print(groupCount)
print(maxValue)