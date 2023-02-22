import sys

s = sys.stdin.readline().rstrip()
count = 0

while "c=" in s:
	s = s.replace("c=", " ", 1)
	count += 1

while "c-" in s:
	s = s.replace("c-", " ", 1)
	count += 1

while "dz=" in s:
	s = s.replace("dz=", " ", 1)
	count += 1

while "d-" in s:
	s = s.replace("d-", " ", 1)
	count += 1

while "lj" in s:
	s = s.replace("lj", " ", 1)
	count += 1

while "nj" in s:
	s = s.replace("nj", " ", 1)
	count += 1

while "s=" in s:
	s = s.replace("s=", " ", 1)
	count += 1

while "z=" in s:
	s = s.replace("z=", " ", 1)
	count += 1

s = s.replace(" ", "")
print(count + len(s))