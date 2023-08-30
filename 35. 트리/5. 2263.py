import sys
sys.setrecursionlimit(10**6)

def change_preOrder(in1: int, in2: int, post1: int, post2: int):
    if in1 > in2 or post1 > post2:
        return

    rootValue = postOrder[post2]
    rootIndex = correctionInOrder[rootValue]

    print(rootValue, end = " ")
    correction = rootIndex - in1
    change_preOrder(in1, rootIndex-1, post1, post1+correction-1)
    change_preOrder(rootIndex+1, in2, post1+correction, post2-1)
    return

n = int(sys.stdin.readline().rstrip())
inOrder = list(map(int, sys.stdin.readline().rstrip().split()))
postOrder = list(map(int, sys.stdin.readline().rstrip().split()))

correctionInOrder = [0] * (n+1)
for i in range(n):
    correctionInOrder[inOrder[i]] = i

change_preOrder(0, n-1, 0, n-1)