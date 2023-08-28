import sys

while 1:
    ab = sys.stdin.readline().rstrip().split()
    a = int(ab[0])
    b = int(ab[1])
    if a == 0 and b == 0:
        break
    elif a > b and a % b == 0:
        print("multiple")
    elif a < b and b % a == 0:
        print("factor")
    else:
        print("neither")