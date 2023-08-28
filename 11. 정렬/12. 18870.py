import sys

n = int(sys.stdin.readline().rstrip())
list = list(map(int, sys.stdin.readline().split()))

set = set(list)
set = [*set]
set.sort()

dic = {set[i] : i for i in range(len(set))}
for i in list:
    print(dic[i], end = ' ')