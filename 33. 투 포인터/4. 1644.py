import sys

BASELEN = 12
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def miller_rabin(n: int):
    if n == 2 or n == 3:
        return True

    if n == 1 or n % 2 == 0:
        return False

    k = 0
    q = n - 1
    while q % 2 == 0:
        k += 1
        q //= 2

    inconclusive = 0
    for i in range(BASELEN):
        if a[i] < n - 1:
            inconclusive = 0

            if pow(a[i], q, n) == 1:
                inconclusive = 1
                continue

            for j in range(k):
                if (pow(pow(a[i], q, n), pow(2, j, n - 1), n) == n - 1):
                    inconclusive = 1
                    break

        if (inconclusive == 0):
            return False
    return True

n = int(sys.stdin.readline().rstrip())
prime_array = []
for i in range(2, n+1):
    if miller_rabin(i):
        prime_array.append(i)

start = 0
end = 0
sum = 0
count = 0
length = len(prime_array)

while end < length:
    if sum <= n:
        sum += prime_array[end]
        end += 1
    else:
        sum -= prime_array[start]
        start +=1

    if sum == n:
        count += 1

while start < length:
    sum -= prime_array[start]
    start +=1

    if sum == n:
        count += 1

print(count)