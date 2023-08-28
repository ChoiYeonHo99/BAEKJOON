import sys

nm = list(map(int, sys.stdin.readline().rstrip().split()))
n = nm[0]
m = nm[1]

dic = {}
for i in range(0, n):
    s = sys.stdin.readline().rstrip()
    dic[s] = i+1
    dic[str(i+1)] = s


for i in range(0, m):
    s = sys.stdin.readline().rstrip()
    print(dic[s])