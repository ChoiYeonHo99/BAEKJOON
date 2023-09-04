import sys

weightNum = int(sys.stdin.readline().rstrip())
weight = list(map(int, sys.stdin.readline().rstrip().split()))
possibelWeight = set([])
for i in range(weightNum):
    temp = list(possibelWeight)
    for j in range(len(temp)):
        possibelWeight.add(temp[j] + weight[i])
        possibelWeight.add(temp[j] - weight[i])
    possibelWeight.add(-weight[i])
    possibelWeight.add(weight[i])

beadNum = int(sys.stdin.readline().rstrip())
bead = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(beadNum):
    if bead[i] in possibelWeight:
        print("Y", end = " ")
    else:
        print("N", end = " ")