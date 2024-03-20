import sys

n = int(sys.stdin.readline().rstrip())
fibonacci = [1] * (n+1)
for i in range(3, n+1):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

print(fibonacci[n])
print(n-2)