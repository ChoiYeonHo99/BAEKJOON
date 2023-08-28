import sys
import math

n = 1000000 + 1
primeList = [True] * n
primeList[0] = False
primeList[1] = False
sqrt = int(math.sqrt(n))
for i in range(2, sqrt+1):
    if primeList[i] == True:
        for j in range(2*i, n, i):
            primeList[j] = False

t = int(sys.stdin.readline().rstrip())
for i in range(0, t):
    m = int(sys.stdin.readline().rstrip())
    a = m // 2
    count = 0
    while 1:
        b = m - a
        if primeList[a] and primeList[b]:
            count += 1
        a -= 1
        if a <= 1:
            break
    print(count)