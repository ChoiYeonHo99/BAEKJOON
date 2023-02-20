def d(n):
	result = n
	str_n = str(n)
	len_n = len(str_n)
	for i in range(0, len_n):
		result += int(str_n[i])
	return result

selfNumber = set([])
for i in range(0, 10001):
	selfNumber.add(d(i))

for i in range(0, 10001):
	if i not in selfNumber:
		print(i)