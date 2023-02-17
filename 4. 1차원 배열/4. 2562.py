import sys

array_n = []

for i in range(0, 9):
	n = int(sys.stdin.readline().rstrip())
	array_n.append(n)

max = array_n[0]
index = 1

for i in range(1, 9):
	if max < array_n[i]:
		max = array_n[i]
		index = i + 1

print(max)
print(index)