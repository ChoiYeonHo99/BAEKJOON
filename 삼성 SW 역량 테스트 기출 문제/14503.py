import sys

def searchBlank():
    for i in range(4):
        dx = directionX[i]
        dy = directionY[i]
        if room[r+dx][c+dy] == 0:
            return True
    return False

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
directionX = [-1, 0, 1, 0]
directionY = [0, 1, 0, -1]
room = []
for _ in range(N):
    room.append(list(map(int, sys.stdin.readline().rstrip().split())))

count = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1
    
    if not searchBlank():
        reverse = (d + 2) % 4
        dx = directionX[reverse]
        dy = directionY[reverse]
        if room[r+dx][c+dy] != 1:
            r += dx
            c += dy
            continue
        else:
            break
    else:
        d = (d+3) % 4
        dx = directionX[d]
        dy = directionY[d]
        if room[r+dx][c+dy] == 0:
            r += dx
            c += dy

print(count)