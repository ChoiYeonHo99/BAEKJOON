import sys

while 1:
	try:
		s = sys.stdin.readline().rstrip().split(" ")
		a = int(s[0])
		b = int(s[1])
		print(a + b)
	except:
		break