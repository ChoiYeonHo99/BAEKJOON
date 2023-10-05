import sys

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

def printNode(node: Node, length: int):
    for child in sorted(node.children.keys()):
        print("--" * length + child)
        printNode(node.children[child], length+1)

N = int(sys.stdin.readline().rstrip())
head = Node(None)
for _ in range(N):
    line = list(sys.stdin.readline().rstrip().split())
    m = int(line[0])
    current_node = head
    for i in range(m):
        if line[i+1] in current_node.children:
            current_node = current_node.children[line[i+1]]
        else:
            current_node.children[line[i+1]] = Node(line[i+1])
            current_node = current_node.children[line[i+1]]

printNode(head, 0)