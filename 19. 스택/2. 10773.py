import sys

stack = []
k = int(sys.stdin.readline().rstrip())

for i in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        del stack[len(stack)-1]
    else:
        stack.append(n)

sum = 0
for i in stack:
    sum += i

print(sum)