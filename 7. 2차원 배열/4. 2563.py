import sys

a = [[0 for i in range(100)] for j in range(100)]

n = int(sys.stdin.readline().rstrip())
for k in range(0, n):
	s = sys.stdin.readline().rstrip().split()
	x = int(s[0])
	y = int(s[1])
	for i in range(x, x+10):
		for j in range(y, y+10):
			a[i][j] = 1

area = 0
for i in range(0, 100):
	for j in range(0, 100):
		if a[i][j] == 1:
			area += 1

print(area)