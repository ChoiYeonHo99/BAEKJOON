import sys

num = [0] * 21
m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    line = list(sys.stdin.readline().rstrip().split())
    command = line[0]
    if command != "all" and command != "empty":
        x = int(line[1])

    if command == "add":
        num[x] = 1
    elif command == "remove":
        num[x] = 0
    elif command == "check":
        if num[x] == 1:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if num[x] == 1:
            num[x] = 0
        else:
            num[x] = 1
    elif command == "all":
        num = [1] * 21
    elif command == "empty":
        num = [0] * 21