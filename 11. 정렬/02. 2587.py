import sys

list = []
for i in range(0, 5):
    a = int(sys.stdin.readline().rstrip())
    list.append(a)

sum = 0
for i in range(0, 5):
    sum += list[i]

sum = int(sum / 5)
list.sort()
print(sum)
print(list[2])