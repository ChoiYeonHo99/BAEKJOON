import sys

n = int(sys.stdin.readline().rstrip())

list = []
count = [0] * 8001
sum = 0
for i in range(0, n):
    a = int(sys.stdin.readline().rstrip())
    sum += a
    list.append(a)
    if a < 0:
        count[a + 8001] += 1
    else:
        count[a] += 1

maxCount = max(count)
mode = []
for i in range(0, 8001):
    if count[i] == maxCount:
        if i > 4000:
            mode.append(i - 8001)
        else:
            mode.append(i)

mode.sort()
list.sort()
print(round(sum / n))
print(list[n // 2])
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])
print(list[n-1] - list[0])