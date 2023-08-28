import sys

n = int(sys.stdin.readline().rstrip())
sCards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
vCards = list(map(int, sys.stdin.readline().rstrip().split()))

dic = {}
for i in sCards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in vCards:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")