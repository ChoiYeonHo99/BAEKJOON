import sys
import math

X, Y, D, T = map(int, sys.stdin.readline().rstrip().split())
remain = math.sqrt(X**2 + Y**2)
result = 0.0
isfirst = True
isosceles = 0
if D / T <= 1:
    print(remain)
else:
    while remain >= D:
        if 2 * D > remain and isfirst:
            isosceles = result
            isfirst = False
        remain -= D
        result += T
    result += min(abs(remain - D) + T, remain)
    print(min(result, isosceles + 2 * T))