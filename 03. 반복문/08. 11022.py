import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
	s = sys.stdin.readline().rstrip().split()
	A = int(s[0])
	B = int(s[1])
	print("Case #" + str(i) + ": " + str(A) + " + " + str(B) + " = " + str(A + B))
