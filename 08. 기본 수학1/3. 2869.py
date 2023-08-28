import sys

s = sys.stdin.readline().rstrip().split()
a = int(s[0])
b = int(s[1])
v = int(s[2])

h = a - b
day = 0
if a >= v:
	day = 1
elif (v - a) // h == 0:
	day = 2
else:
	if (v - a) % h > 0:
		day = (v - a) // h + 2
	else:
		day = (v - a) // h + 1

print(day)