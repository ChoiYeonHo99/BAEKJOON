import sys

def factorial(n: int):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

k = int(sys.stdin.readline().rstrip())

for i in range(k):
    nm = list(map(int, sys.stdin.readline().rstrip().split()))
    n = nm[0]
    m = nm[1]
    print(factorial(m) // (factorial(n) * factorial(m - n)))