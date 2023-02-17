import sys

array_n = [0] * 30
a = 0
b = 0

for i in range(0, 28):
	n = int(sys.stdin.readline().rstrip())
	array_n[n-1] = 1

for i in range(0, 30):
	if array_n[i] == 0:
		if a == 0:
			a = i + 1
		else:
			b = i + 1

if a < b:
	print(a, b)
else:
	print(b, a)