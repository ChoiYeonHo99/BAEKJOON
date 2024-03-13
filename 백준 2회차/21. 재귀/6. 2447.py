import sys

def star(n: int):
    if n == 1:
        return "*"
    
    tmp = star(n//3)
    line = []

    for i in tmp:
        line.append(i * 3)
    for i in tmp:
        line.append(i + " " * (n // 3) + i)
    for i in tmp:
        line.append(i * 3)

    return line

n = int(sys.stdin.readline().strip())
print('\n'.join(star(n)))