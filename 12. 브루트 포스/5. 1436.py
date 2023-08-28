import sys

s = int(sys.stdin.readline().rstrip())
n = 666
count = 0
while 1:
    if "666" in str(n):
        count += 1
    if s == count:
        break
    n += 1
print(n)