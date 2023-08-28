import sys

n = int(sys.stdin.readline().rstrip())

for i in range(0, n):
	s = sys.stdin.readline().rstrip().split()
	A = int(s[0])
	B = int(s[1])
	print(A + B)