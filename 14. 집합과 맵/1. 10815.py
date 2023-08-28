import sys

n = int(sys.stdin.readline().rstrip())
sCards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
vCards = list(map(int, sys.stdin.readline().rstrip().split()))

dic = {sCards[i] : 1 for i in range(len(sCards))}
for i in vCards:
    if i in dic:
        print(1, end = " ")
    else:
        print(0, end = " ")