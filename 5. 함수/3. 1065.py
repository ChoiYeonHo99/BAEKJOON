import sys

def hansu(n):
	str_n = str(n)
	len_n = len(str_n)
	if len_n <= 2:
		return True

	temp = int(str_n[1]) - int(str_n[0])
	for i in range(0, len_n-1):
		difference = int(str_n[i+1]) - int(str_n[i])
		if difference != temp:
			return False
		temp = difference
	return True

count = 0
n = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
	if hansu(i):
		count += 1

print(count)