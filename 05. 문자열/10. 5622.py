import sys

def dial(n : str):
	if n == "A" or n == "B" or n == "C":
		return 3
	elif n == "D" or n == "E" or n == "F":
		return 4
	elif n == "G" or n == "H" or n == "I":
		return 5
	elif n == "J" or n == "K" or n == "L":
		return 6
	elif n == "M" or n == "N" or n == "O":
		return 7
	elif n == "P" or n == "Q" or n == "R" or n == "S":
		return 8
	elif n == "T" or n == "U" or n == "V":
		return 9
	elif n == "W" or n == "X" or n == "Y" or n == "Z":
		return 10
	else:
		return 11

s = sys.stdin.readline().rstrip()
result = 0
for i in range(0, len(s)):
	result += dial(s[i])
print(result)