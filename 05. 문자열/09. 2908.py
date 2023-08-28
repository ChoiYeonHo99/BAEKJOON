import sys

s = sys.stdin.readline().rstrip().split(" ")
a = int(s[0][::-1])
b = int(s[1][::-1])

if a > b:
	print(a)
else:
	print(b)