import sys

L = int(sys.stdin.readline().rstrip())
AD = sys.stdin.readline().rstrip()

F = [0] * L
j = 0
for i in range(1, L):
    while j > 0 and AD[i] != AD[j]:
        j = F[j-1]
    
    if AD[i] == AD[j]:
        j += 1
        F[i] = j

print(L - F[-1])