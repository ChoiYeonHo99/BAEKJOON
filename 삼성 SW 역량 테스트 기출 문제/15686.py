import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
house = []
chicken = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if line[j] == 1:
            house.append((i, j))
        if line[j] == 2:
            chicken.append((i, j))

comb_chicken = list(combinations(chicken, M))
result = N**4
for test_chicken in comb_chicken:
    minValue = [N**2] * len(house)
    for i in range(len(house)):
        for j in range(len(test_chicken)):
            minValue[i] = min(minValue[i], abs(house[i][0] - test_chicken[j][0]) + abs(house[i][1] - test_chicken[j][1]))
    result = min(result, sum(minValue))

print(result)