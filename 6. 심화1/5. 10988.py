import sys

palindrome = True

s = sys.stdin.readline().rstrip()
for i in range(0, int(len(s) / 2)):
	if s[i] != s[len(s)-1-i]:
		palindrome = False

if palindrome:
	print(1)
else:
	print(0)