import sys

nm = sys.stdin.readline().rstrip().split()
n = int(nm[0])
m = int(nm[1])

array = []
for a in range(0, n+1):
	array.append(a)

for a in range(0, m):
	s = sys.stdin.readline().rstrip().split()
	i = int(s[0])
	j = int(s[1])
	k = int(s[2])

	temp = []
	for b in range(0, n+1):
		temp.append(array[b])
	
	count = 0
	for b in range(i, i+j-k+1):
		array[b] = temp[k + count]
		count += 1
		
	count = 0
	for b in range(i+j-k+1, j+1):
		array[b] = temp[i + count]
		count += 1

result = ""
for a in range(1, n):
	result += str(array[a]) + " "
result += str(array[n])
print(result)