import sys

def check(x: int, y: int):
    for i, j in queen:
        if i == x or j == y:
            return False
        if abs(i-x) == abs(j-y):
            return False
    return True

def nQueen(x: int):
    if len(queen) == n:
        global count
        count += 1
        return
    
    if x >= n:
        return

    for j in range(n):
        if yPosition[j] and check(x, j):
            yPosition[j] = False
            queen.append((x, j))
            nQueen(x+1)
            yPosition[j] = True
            queen.pop()

n = int(sys.stdin.readline().rstrip())
queen = []
yPosition = [True] * n
count = 0
nQueen(0)
print(count)