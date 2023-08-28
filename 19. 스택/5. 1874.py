import sys

n = int(sys.stdin.readline().rstrip())
n_list = [i for i in range(1, n+1)]
stack = []
result = []

def push():
    a = n_list[0]
    stack.append(n_list[0])
    del n_list[0]
    result.append("+")
    return a

def pop():
    del stack[len(stack)-1]
    result.append("-")
    if len(stack) == 0:
        return 0
    else:
        return stack[len(stack)-1]

tail = 0
possibility = True
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if tail < num:
        while tail != num:
            if len(n_list) == 0:
                possibility = False
                break
            tail = push()
        if tail == num:
            tail = pop()
    elif tail > num:
        while tail != num:
            if len(n_list) == 0:
                possibility = False
                break
            tail = pop()
        if tail == num:
            tail = pop()
    elif tail == num:
        tail = pop()

if possibility:
    for i in result:
        print(i, end = "\n")
else:
    print("NO")