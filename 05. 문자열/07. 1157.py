import sys

s = sys.stdin.readline().rstrip().lower()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
result = [0] * len(alphabet)

for i in range(0, len(alphabet)):
	for j in range(0, len(s)):
		if alphabet[i] == s[j]:
			result[i] += 1

max = result[0]
index = 0
joint = False
for i in range(1, len(alphabet)):
	if result[i] == max:
		joint = True
	elif result[i] > max:
		max = result[i]
		index = i
		joint = False

if joint == True:
	print("?")
else:
	print(alphabet[index].upper())