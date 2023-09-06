import sys
import math

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().rstrip().split())

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if d >= r1 + r2:
    print("0.000")
elif d <= abs(r1 - r2):
    print(round(min(r1, r2)**2 * math.pi, 3))
else:
    a1 = 2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    a2 = 2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
    s = (r1**2 * (a1 - math.sin(a1)) + r2**2 * (a2 - math.sin(a2))) / 2
    print(round(s, 3))