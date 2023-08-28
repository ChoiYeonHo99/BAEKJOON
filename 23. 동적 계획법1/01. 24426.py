import sys

n = int(sys.stdin.readline().rstrip())
f = [1] * n
for i in range(3, n):
    f[i] = f[i-1] + f[i-2]

print(f[n-1] + f[n-2])
print(n-2)