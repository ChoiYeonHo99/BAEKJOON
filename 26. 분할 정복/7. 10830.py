import sys

n, b = map(int, sys.stdin.readline().rstrip().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

def mul(a, b):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                result[i][j] += a[i][x] * b[x][j]
            result[i][j] = result[i][j] % 1000
    return result

def calculation(b):
    if b == 1:
        return a
    half = calculation(b // 2)
    result = mul(half, half)
    if b % 2 == 1:
        result = mul(result, a)
    return result

result = calculation(b)
for i in range(n):
    for j in range(n):
        result[i][j] = result[i][j] % 1000
for x in result:
    print(*x)