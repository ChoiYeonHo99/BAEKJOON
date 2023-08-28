import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip().split()
count = 0

for i in range(0, n):
    a = int(s[i])
    
    if a == 1:
        continue
    elif a == 2:
        count += 1
        continue
    
    prime = True
    for j in range(2, a // 2 + 1):
        if a % j == 0:
            prime = False
            break

    if prime:
        count += 1

print(count)