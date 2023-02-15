x = input().split(" ")
h = int(x[0])
m = int(x[1]) - 45

if m >= 0:
	print(h, m)
else:
	m += 60
	h -= 1
	if h >= 0:
		print(h, m)
	else:
		h += 24
		print(h, m)