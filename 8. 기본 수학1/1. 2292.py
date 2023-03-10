import sys

n = int(sys.stdin.readline().rstrip())

count = 1
distance = 1
while n > 1:
	n -= 6 * count
	count += 1
	distance += 1

print(distance)