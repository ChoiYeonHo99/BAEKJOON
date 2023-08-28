import sys

def calculation(blocks: list, n: int):
    stack = []
    maxValue = 0
    index = 0

    while index < n:
        if not stack or blocks[index] >= blocks[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = blocks[top] * width
            maxValue = max(maxValue, area)

    while stack:
        top = stack.pop()
        width = index if not stack else n - stack[-1] - 1
        area = blocks[top] * width
        maxValue = max(maxValue, area)

    return maxValue

while 1:
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    if line[0] == 0:
        break
    n = line[0]
    blocks = line[1:]
    result = calculation(blocks, n)
    print(result)