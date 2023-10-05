import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

n = len(T)
m = len(P)
pi = [0] * m
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j - 1]

    if (P[i] == P[j]):
        j += 1
        pi[i] = j

j = 0
count = 0
record = []
for i in range(n):
    while j > 0 and T[i] != P[j]:
        j = pi[j-1]

    if T[i] == P[j]:
        if j == m-1:
            count += 1
            record.append(i-m+2)
            j = pi[j]
        else:
            j += 1

print(count)
print(*record)