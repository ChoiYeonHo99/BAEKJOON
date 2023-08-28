import sys

a = [[0 for i in range(3)] for j in range(3)]

for i in range(0, 3):
	row = sys.stdin.readline().rstrip().split()
	for j in range(0, 3):
		a[i][j] = int(row[j])

max = a[0][0]
index_x = 0
index_y = 0

for i in range(0, 3):
	for j in range(0, 3):
		if max < a[i][j]:
			max = a[i][j]
			index_x = i
			index_y = j

print(max)
print(index_x + 1, index_y + 1)
