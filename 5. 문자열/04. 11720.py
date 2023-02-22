import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
result = 0

for i in range(0, n):
	result += int(s[i])

print(result)