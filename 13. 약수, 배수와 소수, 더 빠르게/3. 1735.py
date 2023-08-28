import sys

a = list(map(int, sys.stdin.readline().rstrip().split()))
a1 = a[0]
a2 = a[1]
b = list(map(int, sys.stdin.readline().rstrip().split()))
b1 = b[0]
b2 = b[1]

r = 1
if a2 > b2:
    while r != 0:
        r = a2 % b2
        if r == 0:
            gcd = b2
            break
        a2 = b2
        b2 = r
else:
    while r != 0:
        r = b2 % a2
        if r == 0:
            gcd = a2
            break
        b2 = a2
        a2 = r
a2 = a[1]
b2 = b[1]
gcd = int(a2 * b2 / gcd)

a1 *= int(gcd / a2)
b1 *= int(gcd / b2)
numerator = a1 + b1
denominator = gcd

r = 1
while r != 0:
    r = denominator % numerator
    if r == 0:
        gcd2 = numerator
        break
    denominator = numerator
    numerator = r

numerator = int((a1 + b1) / gcd2)
denominator = int(gcd / gcd2)
print(numerator, denominator)