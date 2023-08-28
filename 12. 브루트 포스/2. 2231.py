import sys

n = int(sys.stdin.readline().rstrip())
isit = False
for i in range(n):
    sum = i
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if sum == n:
        print(i)
        isit = True
        break

if isit == False:
    print(0)