import sys

nm = sys.stdin.readline().rstrip().split()
n = int(nm[0])
m = int(nm[1])
array = [0] * n

for a in range(0, m):
	ijk = sys.stdin.readline().rstrip().split()
	i = int(ijk[0])
	j = int(ijk[1])
	k = int(ijk[2])
	for b in range(i, j+1):
		array[b-1] = k

result = ""
for i in range(0, n-1):
	result += str(array[i]) + " "

result += str(array[n-1])
print(result)