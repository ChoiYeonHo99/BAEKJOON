import sys

m = 1000000007

def factorial(n: int):
    result = 1
    for i in range(1, n+1):
        result = result * i % m
    return result

def calculation(a, b, c):
    if b == 0:
        return 1
    
    half = calculation(a, b // 2, c)
    result = (half * half) % c

    if b % 2 == 1:
        result = (result * a) % c
    return result

n, k = map(int, sys.stdin.readline().rstrip().split())
a = factorial(n)
b = calculation(factorial(k), m-2, m)
c = calculation(factorial(n-k), m-2, m)
print(a*b*c%m)