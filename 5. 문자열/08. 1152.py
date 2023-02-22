import sys

s = sys.stdin.readline().rstrip().split(" ")
if s[0] == "":
	print(len(s) - 1)
else:
	print(len(s))