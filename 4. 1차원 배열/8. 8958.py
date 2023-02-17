import sys

n = int(sys.stdin.readline().rstrip())
total = 0
continuous = 1
s = ""
for i in range(0, n):
	s = sys.stdin.readline().rstrip()
	for j in range(0, len(s)):
		if s[j] == "O":
			total += continuous
			continuous += 1
		else:
			continuous = 1
	print(total)
	total = 0
	continuous = 1
			