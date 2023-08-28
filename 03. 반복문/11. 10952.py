import sys

while 1:
	s = sys.stdin.readline().rstrip().split(" ")
	a = int(s[0])
	b = int(s[1])
	if a == 0 and b == 0:
		break
	else:
		print(a + b)