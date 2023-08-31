import sys
import math
from itertools import permutations

def Calculation(y1: int, b: int, x3: int):
    x1 = 0
    x2 = b / math.sqrt(2)
    y2 = b / math.sqrt(2)
    y3 = 0
    comp = (y2 - y1) * (x3 - x2) - (y3 - y2) * (x2 - x1)

    if comp > 0:
        return True
    else:
        return False

ability = list(map(int, sys.stdin.readline().rstrip().split()))
all_permutations = permutations(ability)
count = 0
for perm in all_permutations:
    possible = True
    for i in range(8):
        if not Calculation(perm[i], perm[(i+1)%8], perm[(i+2)%8]):
            possible = False
            break
    if possible:
        count += 1

print(count)