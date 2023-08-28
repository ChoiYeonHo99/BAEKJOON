import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    a = [[0 for x in range(n+1)] for y in range(k+1)]
    for x in range(n+1):
        a[0][x] = x
    for y in range(1, k+1):
        for x in range(1, n+1):
            sum = 0
            for z in range(1, x+1):
                sum += a[y-1][z]
            a[y][x] = sum
    print(a[k][n])