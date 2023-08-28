import sys

n = int(sys.stdin.readline().rstrip())
count = 0

for i in range(0, n):
	s = sys.stdin.readline().rstrip()
	array = []
	array.append(s[0])

	group = True
	for j in range(1, len(s)):
		if s[j] != s[j-1]:
			if s[j] in array:
				group = False
			else:
				array.append(s[j])

	if group == True:
		count += 1

print(count)