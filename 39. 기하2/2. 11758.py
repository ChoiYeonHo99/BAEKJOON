import sys

position = []
for _ in range(3):
    position.append(list(map(int, sys.stdin.readline().rstrip().split())))

comp = (position[1][1] - position[0][1]) * (position[2][0] - position[1][0]) - (position[2][1] - position[1][1]) * (position[1][0] - position[0][0])
if comp == 0:
    print(0)
elif comp > 0:
    print(-1)
else:
    print(1)