import sys

def factorial(n: int):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


nk = list(map(int, sys.stdin.readline().rstrip().split()))
n = nk[0]
k = nk[1]

print(factorial(n) // (factorial(k) * factorial(n - k)))