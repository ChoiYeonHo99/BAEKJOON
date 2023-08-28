import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
num_array = list(map(int, sys.stdin.readline().rstrip().split()))
dic = {}
for i in num_array:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

result = [0] * n
stack = deque([])

for i in range(n):
    if len(stack) == 0:
        stack.append(i)
        continue

    index = stack.pop()
    while dic[num_array[index]] < dic[num_array[i]]:
        result[index] = num_array[i]
        if len(stack) == 0:
            stack.append(i)
            break
        else:
            index = stack.pop()
    else:
        stack.append(index)
        stack.append(i)

for i in range(len(stack)):
    index = stack.pop()
    result[index] = -1

for i in result:
    print(i, end = " ")