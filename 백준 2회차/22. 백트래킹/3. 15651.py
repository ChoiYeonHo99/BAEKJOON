import sys

def nm(a: int):
    if a > m:
        print(*line)
        return

    for i in range(1, n+1):
        line.append(i)
        nm(a+1)
        line.pop()

n, m = map(int, sys.stdin.readline().rstrip().split())
line = []
nm(1)