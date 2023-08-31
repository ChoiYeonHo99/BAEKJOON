import sys

n = int(sys.stdin.readline().rstrip())
position = []
for _ in range(n):
    position.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = 0
for i in range(1, n-1):
    result += (position[i][0]-position[0][0])*(position[i+1][1]-position[0][1]) - (position[i+1][0]-position[0][0])*(position[i][1]-position[0][1])

print(round(abs(result) / 2, 1))