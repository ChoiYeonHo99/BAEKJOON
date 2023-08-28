import sys

nm = sys.stdin.readline().rstrip().split()
n = int(nm[0])
m = int(nm[1])

a = [[0 for j in range(m)] for i in range(n)]
b = [[0 for j in range(m)] for i in range(n)]
c = [[0 for j in range(m)] for i in range(n)]

for i in range(0, n):
	row = sys.stdin.readline().rstrip().split()
	for j in range(0, m):
		a[i][j] = int(row[j])

for i in range(0, n):
	row = sys.stdin.readline().rstrip().split()
	for j in range(0, m):
		b[i][j] = int(row[j])

for i in range(0, n):
	for j in range(0, m):
		c[i][j] = a[i][j] + b[i][j]

for i in range(0, n):
	result = ""
	for j in range(0, m):
		result += str(c[i][j]) + " "
	print(result.rstrip())