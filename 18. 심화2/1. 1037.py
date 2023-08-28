import sys


number = int(sys.stdin.readline().rstrip())
n = list(map(int, sys.stdin.readline().rstrip().split()))
n.sort()

if number == 1:
    print(n[0] ** 2)
else:
    print(n[0] * n[len(n)-1])