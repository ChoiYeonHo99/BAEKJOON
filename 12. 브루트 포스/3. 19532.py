import sys

s = list(map(int, sys.stdin.readline().split()))
a = s[0]
b = s[1]
c = s[2]
d = s[3]
e = s[4]
f = s[5]

x = (c * e - f * b) / (a * e - d * b)
y = (c * d - f * a) / (b * d - e * a)
print(int(x), int(y))