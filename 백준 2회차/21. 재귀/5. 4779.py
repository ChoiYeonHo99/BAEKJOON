import sys

def cantor(n: int):
    if n == 0:
        print("-", end = "")
    else:
        cantor(n-1)
        for i in range(3**(n-1)):
            print(" ", end = "")
        cantor(n-1)

while 1:
    try:
        n = int(sys.stdin.readline().rstrip())
        cantor(n)
        print()
    except ValueError:
        break