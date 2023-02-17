import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip().split()
v = int(sys.stdin.readline().rstrip())
count = 0

for i in range(0, n):
	if (int(s[i]) == v):
		count += 1

print(count)