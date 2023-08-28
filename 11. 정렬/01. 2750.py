import sys

n = int(sys.stdin.readline().rstrip())
list = []
for i in range(0, n):
    a = int(sys.stdin.readline().rstrip())
    list.append(a)

list.sort()
for i in range(0, n):
    print(list[i])