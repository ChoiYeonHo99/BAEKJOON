import sys

n = int(sys.stdin.readline())
dic = {}
count = 0
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name == "ENTER":
        dic = {}
    else:
        if not name in dic:
            count += 1
            dic[name] = 1

print(count)