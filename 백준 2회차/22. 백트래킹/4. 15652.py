import sys

def nm(a: int, b: int):
    if a > m:
        print(*line)
        return

    for i in range(b, n+1):
        line.append(i)
        nm(a+1, i)
        line.pop()

n, m = map(int, sys.stdin.readline().rstrip().split())
line = []
nm(1, 1)