import sys

nm = sys.stdin.readline().rstrip().split()
n = int(nm[0])
m = int(nm[1])
array = [0] * (n+1)

for a in range(0, n+1):
	array[a] = a

for a in range(0, m):
	ij = sys.stdin.readline().rstrip().split()
	i = int(ij[0])
	j = int(ij[1])
	count = 0
	for b in range(i, int((i+j) / 2) + 1):
		temp = array[b]
		array[b] = array[j-count]
		array[j-count] = temp
		count += 1

result = ""
for i in range(1, n):
	result += str(array[i]) + " "

result += str(array[n])
print(result)