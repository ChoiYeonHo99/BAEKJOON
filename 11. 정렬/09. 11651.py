import sys

n = int(sys.stdin.readline().rstrip())
coordinate = []

for i in range(n):
    xy = sys.stdin.readline().rstrip().split()
    x = int(xy[0])
    y = int(xy[1])
    coordinate.append([y, x])

coordinate.sort()
for i in range(n):
    string = str(coordinate[i][1]) + " " + str(coordinate[i][0])
    print(string)