import sys

nm = list(map(int, sys.stdin.readline().rstrip().split()))
n = nm[0]
m = nm[1]
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

dic_a = {a[i] : 1 for i in range(n)}
dic_b = {b[i] : 1 for i in range(m)}

count = 0
for i in range(n):
    if a[i] not in dic_b:
        count += 1

for i in range(m):
    if b[i] not in dic_a:
        count += 1

print(count)