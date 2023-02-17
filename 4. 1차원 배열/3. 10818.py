import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip().split(" ")

max = int(s[0])
min = int(s[0])

for i in range(1, n):
	if max < int(s[i]):
		max = int(s[i])
	if min > int(s[i]):
		min = int(s[i])

print(min, max)