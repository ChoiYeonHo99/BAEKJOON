import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    stack = []
    vps = True
    ps = sys.stdin.readline().rstrip()
    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                vps = False
                break
            else:
                del stack[len(stack)-1]

    if vps and len(stack) == 0:
        print("YES")
    else:
        print("NO")