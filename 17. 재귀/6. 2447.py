import sys

def drowStar(n: int):
    if n == 1:
        return "*"
    
    part = drowStar(n//3)
    star = []

    for i in part:
        star.append(i * 3)
    for i in part:
        star.append(i + " " * (n // 3) + i)
    for i in part:
        star.append(i * 3)

    return star

n = int(sys.stdin.readline().strip())
print('\n'.join(drowStar(n)))