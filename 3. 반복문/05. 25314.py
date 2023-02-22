import sys

n = int(sys.stdin.readline().rstrip())
result = ""
for i in range(0, n // 4):
	result += "long "
	
print(result + "int")
