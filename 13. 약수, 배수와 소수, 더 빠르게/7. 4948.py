import sys
import math

n = 123456 * 2 + 1
primeList = [True] * n
primeList[0] = False
primeList[1] = False
sqrt = int(math.sqrt(n))
for i in range(2, sqrt+1):
    if primeList[i] == True:
        for j in range(2*i, n, i):
            primeList[j] = False

while 1:
    m = int(sys.stdin.readline().rstrip())
    if m == 0:
        break
    count = 0
    for i in range(m+1, 2*m+1):
        if primeList[i] == True:
            count += 1
    print(count)