import sys
import math

def primeFactorization(n: int):
    mod = 2
    primeList = []
    sqrt = math.sqrt(n)
    while n > 1 and mod <= sqrt:
        if n % mod == 0:
            n = n // mod
            primeList.append(mod)
        else:
            mod += 1
    if n != 1:
        primeList.append(n)
    return primeList

t = int(sys.stdin.readline().rstrip())
for i in range(0, t):
    ab = list(map(int, sys.stdin.readline().rstrip().split()))
    a = ab[0]
    b = ab[1]
    aList = primeFactorization(a)
    bList = primeFactorization(b)
    leastCommonMultiple = a
    for j in range(0, len(aList)):
        if aList[j] in bList:
            bList.remove(aList[j])
    for j in range(0, len(bList)):
        leastCommonMultiple *= bList[j]
    print(leastCommonMultiple)