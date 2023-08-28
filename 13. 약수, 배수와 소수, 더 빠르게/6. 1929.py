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

nm = list(map(int, sys.stdin.readline().rstrip().split()))
n = nm[0]
m = nm[1]
for i in range(n, m+1):
    if isPrime(i):
        print(i)