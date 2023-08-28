import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0] * n for _ in range(n)]
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

if n == 1:
    print(0)
    exit()

for i in range(1, n):
    for j in range(i):
        print()