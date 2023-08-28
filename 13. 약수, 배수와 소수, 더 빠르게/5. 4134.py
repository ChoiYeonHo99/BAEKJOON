import sys
import math

def isPrime(n: int):
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

t = int(sys.stdin.readline().rstrip())

for i in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    prime = n
    while 1:
        if isPrime(prime):
            break
        else:
            prime += 1
    print(prime)