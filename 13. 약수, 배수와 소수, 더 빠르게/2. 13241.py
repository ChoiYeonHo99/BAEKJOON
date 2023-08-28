import sys

ab = list(map(int, sys.stdin.readline().rstrip().split()))
a = ab[0]
b = ab[1]

r = 1
if a > b:
    while r != 0:
        r = a % b
        if r == 0:
            gcd = b
            break
        a = b
        b = r
else:
    while r != 0:
        r = b % a
        if r == 0:
            gcd = a
            break
        b = a
        a = r
a = ab[0]
b = ab[1]
gcd = int(a * b / gcd)
print(gcd)