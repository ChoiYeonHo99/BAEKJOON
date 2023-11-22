import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
line = []
input = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    input.append((a, b))

input.sort()
s = input[0][0]
e = input[0][1]
result = 0
for i in range(1, N):
    a = input[i][0]
    b = input[i][1]
    if a > e:
        result += e - s
        s = a
        e = b
    elif b > e:
        e = b

result += e - s
print(result)