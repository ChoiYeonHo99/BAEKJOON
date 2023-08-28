import sys

dic = {}
n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))
for i in m_list:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")