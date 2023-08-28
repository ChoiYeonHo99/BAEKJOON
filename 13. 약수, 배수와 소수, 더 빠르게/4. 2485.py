import sys
t = int(sys.stdin.readline().rstrip())
nowList = []
interval = []
for i in range(0, t):
    nowList.append(int(sys.stdin.readline().rstrip()))

for i in range(0, t-1):
    interval.append(nowList[i+1] - nowList[i])

gcd = 0
r = 1
while r != 0:
    r = interval[1] % interval[0]
    if r == 0:
        gcd = interval[0]
        break
    interval[1] = interval[0]
    interval[0] = r

for i in range(1, t-2):
    r = 1
    while r != 0:
        r = gcd % interval[i+1]
        if r == 0:
            gcd = interval[i+1]
            break
        gcd = interval[i+1]
        interval[i+1] = r

count = 0
for i in range(0, t-1):
    count += int(((nowList[i+1] - nowList[i]) / gcd) - 1)

print(count)