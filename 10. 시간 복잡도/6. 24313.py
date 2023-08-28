import sys

a = sys.stdin.readline().rstrip().split()
a1 = int(a[0])
a0 = int(a[1])
c = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

if (a1 - c) * n + a0 <= 0:
    if c >= a1:
        print(1)
    else:
        print(0)
else:
    print(0)