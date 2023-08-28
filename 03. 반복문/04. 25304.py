X = int(input())
N = int(input())
r = 0

for i in range(0, N):
	s = input().split(" ")
	a = int(s[0])
	b = int(s[1])
	r += a * b

if X == r:
	print("Yes")
else:
	print("No")