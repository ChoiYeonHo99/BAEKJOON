import sys

n = int(sys.stdin.readline())
dic = {}
count = 0
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    if (a == "ChongChong" or b == "ChongChong") and "ChongChong" not in dic:
        dic["ChongChong"] = 1
        count += 1
    if a in dic and not b in dic:
        dic[b] = 1
        count += 1
    elif a not in dic and b in dic:
        dic[a] = 1
        count += 1

print(count)