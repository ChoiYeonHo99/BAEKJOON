import sys

n = sys.stdin.readline().rstrip()
list = []

for i in range(0, len(n)):
    list.append(int(n[i]))

list.sort(reverse=True)
print(*list, sep = "")