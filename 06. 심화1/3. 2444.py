import sys

n = int(sys.stdin.readline().rstrip())
for i in range(0, n):
	print(" " * (n-1-i) + "*" * (2*i+1))

for i in range(0, n-1):
	print(" " * (i+1) + "*" * (2*n-3-2*i))