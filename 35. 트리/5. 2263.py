import sys

def change_preOrder(inOrder: list, postOrder: list):
    if not inOrder or not postOrder:
        return []

    rootValue = postOrder.pop()
    rootIndex = inOrder.index(rootValue)

    root = [rootValue]
    postIndex = 0
    for i in range(len(postOrder)):
        if postOrder[i] > rootValue:
            postIndex = i
            break

    right = change_preOrder(inOrder[rootIndex+1:], postOrder[postIndex:])
    left = change_preOrder(inOrder[:rootIndex], postOrder[:postIndex])

    return root + left + right

n = int(sys.stdin.readline().rstrip())
inOrder = list(map(int, sys.stdin.readline().rstrip().split()))
postOrder = list(map(int, sys.stdin.readline().rstrip().split()))

preOrder = change_preOrder(inOrder, postOrder)
for i in range(len(preOrder)):
    print(preOrder[i], end = " ")