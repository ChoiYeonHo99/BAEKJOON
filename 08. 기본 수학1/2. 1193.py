import sys

x = int(sys.stdin.readline().rstrip())
n = 1

while x > n:
	x -= n
	n += 1

if n % 2 == 0:
	print(str(x) + "/" + str(n+1-x))
else:
	print(str(n+1-x) + "/" + str(x))