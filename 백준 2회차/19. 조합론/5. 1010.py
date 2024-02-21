import sys
import math

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(int(math.factorial(m) / (math.factorial(n) * math.factorial(m-n))))