import sys

def deterministicMillerRabin(n: int):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    
    base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    k = 0
    q = n - 1
    while q % 2 == 0:
        k += 1
        q = q >> 1

    for i in range(0, len(base)):
        if base[i] < n - 1:
            inconclusive = False
            if base[i] ** q % n == 1:
                inconclusive = True
                continue
        for j in range(0, k):
            if (base[i] ** q) ** (2 ** j) % n == n - 1:
                inconclusive = True
                break
        if not inconclusive:
            return False
    return True

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
prime = []
sum = 0

for i in range(m, n+1):
    if deterministicMillerRabin(i):
        prime.append(i)
        sum += i

if sum == 0:
    print("-1")
else:
    print(sum)
    print(prime[0])