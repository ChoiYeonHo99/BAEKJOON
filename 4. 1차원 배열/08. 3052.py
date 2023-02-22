import sys

array_n = []

for i in range(0, 10):
	n = int(sys.stdin.readline().rstrip())
	if n % 42 not in array_n:
		array_n.append(n % 42)

print(len(array_n))