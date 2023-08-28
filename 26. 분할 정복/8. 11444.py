import sys

n = int(sys.stdin.readline().rstrip())
a = [[1, 1], [1, 0]]

def mul(a, b):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for x in range(2):
                result[i][j] += a[i][x] * b[x][j]
            result[i][j] = result[i][j] % 1000000007
    return result

def calculation(b):
    if b == 1:
        return a
    half = calculation(b // 2)
    result = mul(half, half)
    if b % 2 == 1:
        result = mul(result, a)
    return result

result = calculation(n)
for i in range(2):
    for j in range(2):
        result[i][j] = result[i][j] % 1000000007

print(result[0][1])