import sys

n = int(sys.stdin.readline().rstrip())
list = []

for i in range(n):
    agename = sys.stdin.readline().rstrip().split()
    age = int(agename[0])
    name = agename[1]
    list.append([age, name])

list.sort(key=lambda x:x[0])
for i in range(n):
    string = str(list[i][0]) + " " + list[i][1]
    print(string)