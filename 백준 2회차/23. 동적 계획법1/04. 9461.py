import sys

padoban = [1] * 101
padoban[4] = 2
padoban[5] = 2
for i in range(6, 101):
    padoban[i] = (padoban[i-1] + padoban[i-5])

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(padoban[n])