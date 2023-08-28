import sys

n = int(sys.stdin.readline().rstrip())

for i in range(0, n):
	s = sys.stdin.readline().rstrip()
	print(s[0] + s[len(s)-1])