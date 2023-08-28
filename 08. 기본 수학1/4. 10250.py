import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    y = 0
    x = 0
    hwn = sys.stdin.readline().rstrip().split()
    h = int(hwn[0])
    w = int(hwn[1])
    n = int(hwn[2])
    if n % h == 0:
        y = n // h
        x = h
    else:
        y = n // h + 1
        x = n % h
    if y < 10:
        print(str(x) + "0" + str(y))
    else:
        print(str(x) + str(y))