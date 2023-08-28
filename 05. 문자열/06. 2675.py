import sys

t = int(sys.stdin.readline().rstrip())

for i in range(0, t):
	result = ""
	data = sys.stdin.readline().rstrip().split(" ")
	r = int(data[0])
	s = data[1]
	for j in range(0, len(s)):
		result += s[j] * r
	print(result)