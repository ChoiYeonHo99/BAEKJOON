import sys

nx = sys.stdin.readline().rstrip().split(" ")
s = sys.stdin.readline().rstrip().split(" ")

n = int(nx[0])
x = int(nx[1])

r = []
result = ""

for i in range(0, n):
	if (x > int(s[i])):
		r.append(int(s[i]))
		
for i in range(0, len(r)):
	if i == len(r) - 1:
		result += str(r[i])
	else:
		result += str(r[i]) + " "

print(result)