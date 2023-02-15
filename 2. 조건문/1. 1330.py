x = input().split(" ")
A = int(x[0])
B = int(x[1])

if A < B:
	print("<")
elif A > B:
	print(">")
elif A == B:
	print("==")