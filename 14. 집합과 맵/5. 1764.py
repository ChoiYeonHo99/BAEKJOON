import sys

nm = list(map(int, sys.stdin.readline().rstrip().split()))
n = nm[0]
m = nm[1]

dic = {}
for i in range(0, n):
    s = sys.stdin.readline().rstrip()
    dic[s] = 1

count = 0
printList = []
for i in range(0, m):
    s = sys.stdin.readline().rstrip()
    if s in dic:
        count += 1
        printList.append(s)

print(count)
printList.sort()
for i in printList:
    print(i)