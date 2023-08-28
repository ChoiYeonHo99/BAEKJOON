import sys

n = int(sys.stdin.readline().rstrip())
meeting = []
for _ in range(n):
    meet = list(map(int, sys.stdin.readline().rstrip().split()))
    meeting.append(tuple(meet))

meeting.sort()
meeting.sort(key=lambda x: x[1])
time = 0
count = 0
for i in range(n):
    if time <= meeting[i][0]:
        time = meeting[i][1]
        count += 1

print(count)