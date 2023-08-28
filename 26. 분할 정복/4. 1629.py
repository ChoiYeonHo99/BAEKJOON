import sys

def calculation(a, b, c):
    if b == 0:
        return 1 % c

    half = calculation(a, b // 2, c)
    result = (half * half) % c

    if b % 2 == 1:
        result = (result * a) % c

    return result

a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(calculation(a, b, c))