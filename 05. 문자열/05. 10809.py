import sys

s = sys.stdin.readline().rstrip()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(0, len(alphabet)):
	existence = False
	for j in range(0, len(s)):
		if alphabet[i] == s[j]:
			existence = True
			print(j)
			break
	if existence == False:
		print(-1)