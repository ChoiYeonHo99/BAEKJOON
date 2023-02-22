import sys

a = [["" for i in range(15)] for j in range(5)]

for i in range(0, 5):
	row = sys.stdin.readline().rstrip()
	for j in range(0, len(row)):
		a[i][j] = row[j]

result = ""
for j in range(0, 15):
	for i in range(0, 5):
		result += a[i][j]

print(result)