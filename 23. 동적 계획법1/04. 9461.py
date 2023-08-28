import sys

t = int(sys.stdin.readline().rstrip())
padonan = [1, 1, 1, 2, 2]
index = 5

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    if n <= index:
        print(padonan[n-1])
        continue
    for i in range(index, n):
        index += 1
        padonan.append(padonan[i-1] + padonan[i-5])
    print(padonan[n-1])