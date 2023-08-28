import sys

n = int(sys.stdin.readline().rstrip())
list = []

for i in range(n):
    s = sys.stdin.readline().rstrip()
    list.append([len(s), s])

list.sort()
for i in range(n):
    if i > 0:
        if list[i][1] != list[i-1][1]:
            print(list[i][1])
    else:
        print(list[i][1])