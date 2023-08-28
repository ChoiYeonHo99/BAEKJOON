import sys

c = int(sys.stdin.readline().rstrip())
s = []
n = 0
avg = 0
count = 0
for i in range(0, c):
	s = sys.stdin.readline().rstrip().split()
	n = int(s[0])
	for j in range(1, n+1):
		avg += int(s[j])
	avg /= n
	for j in range(1, n+1):
		if avg < int(s[j]):
			count += 1
	print(str(format(count / n * 100, ".3f")) + "%")
	avg = 0
	count = 0