import sys

def calculation(x: int, y: int, d1: int, d2: int):
    team = [[0] * (N+1) for _ in range(N+1)]
    for i in range(d1+1):
        team[x+i][y-i] = 5
    for i in range(d2+1):
        team[x+i][y+i] = 5
    for i in range(d2+1):
        team[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        team[x+d2+i][y+d2-i] = 5

    population = [0] * 5
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if team[r][c] != 5:
                population[0] += city[r][c]
            else:
                break
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if team[r][c] != 5:
                population[1] += city[r][c]
            else:
                break
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if team[r][c] != 5:
                population[2] += city[r][c]
            else:
                break
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if team[r][c] != 5:
                population[3] += city[r][c]
            else:
                break
    
    population[4] = totalPopulation - sum(population)
    return max(population) - min(population)

N = int(sys.stdin.readline())
city = [[0] * (N+1)]
totalPopulation = 0
for i in range(1, N+1):
    city.append([0] + list(map(int, sys.stdin.readline().split())))
    for j in range(1, N+1):
        totalPopulation += city[i][j]

result = totalPopulation
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 <= N and 1 <= y-d1 and y+d2 <= N:
                    result = min(result, calculation(x, y, d1, d2))

print(result)