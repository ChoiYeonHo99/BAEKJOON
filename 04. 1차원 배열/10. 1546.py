import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip().split()

max = int(s[0])
avg = 0

for i in range(0, n):
	if max < int(s[i]):
		max = int(s[i])

for i in range(0, n):
	avg += int(s[i]) / max * 100

print(avg / n)