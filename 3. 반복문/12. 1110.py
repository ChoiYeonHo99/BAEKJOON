import sys

N = int(sys.stdin.readline().rstrip())
n = N
cycle = 0

while 1:
	if n < 10:
		new = 11 * n
	else:
		a = int(str(n)[0]) + int(str(n)[1])
		if a < 10:
			new = 10 * int(str(n)[1]) + a
		else:
			new = 10 * int(str(n)[1]) + int(str(a)[1])
	cycle += 1
	n = new
	if n == N:
		break

print(cycle)