import sys

def factorial(n: int):
    if n == 0:
        return 1
    
    return factorial(n-1) * n

n = int(sys.stdin.readline().rstrip())
print(factorial(n))