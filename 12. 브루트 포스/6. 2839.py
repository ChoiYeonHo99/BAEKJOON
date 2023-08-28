import sys

n = int(sys.stdin.readline().rstrip())
k5 = n // 5
k3 = (n - 5 * k5) // 3
chance = True

while 5 * k5 + 3 * k3 != n:
    k5 -= 1
    k3 = (n - 5 * k5) // 3
    if k5 < 0:
        chance = False
        break

if chance:
    print(k5 + k3)
else:
    print(-1)