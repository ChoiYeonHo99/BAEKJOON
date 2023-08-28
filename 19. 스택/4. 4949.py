import sys

while 1:
    stack = []
    vps = True
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break

    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        elif s[i] == "[":
            stack.append("[")
        elif s[i] == ")":
            if len(stack) == 0 or stack[len(stack)-1] != "(":
                vps = False
                break
            else:
                del stack[len(stack)-1]
        elif s[i] == "]":
            if len(stack) == 0 or stack[len(stack)-1] != "[":
                vps = False
                break
            else:
                del stack[len(stack)-1]
    
    if vps and len(stack) == 0 and s[len(s)-1] == ".":
        print("yes")
    else:
        print("no")