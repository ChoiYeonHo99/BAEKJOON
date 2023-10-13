import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = 0
for i in range(N):
    ramp = [False] * N
    for j in range(N):
        if j == N-1:
            result += 1
            break

        if world[i][j] == world[i][j+1]:
            continue

        elif world[i][j] - world[i][j+1] == 1:
            h = world[i][j+1]
            construction = 0
            for k in range(j+1, N):
                if world[i][k] == h:
                    construction += 1
                    ramp[k] = True
                else:
                    break
                if construction == L:
                    break
            if construction == L:
                continue
            else:
                break

        elif world[i][j] - world[i][j+1] == -1:
            h = world[i][j]
            construction = 0
            for k in range(j, -1, -1):
                if world[i][k] == h and not ramp[k]:
                    construction += 1
                    ramp[k] = True
                else:
                    break
                if construction == L:
                    break
            if construction == L:
                continue
            else:
                break

        else:
            break

for i in range(N):
    ramp = [False] * N
    for j in range(N):
        if j == N-1:
            result += 1
            break

        if world[j][i] == world[j+1][i]:
            continue

        elif world[j][i] - world[j+1][i] == 1:
            h = world[j+1][i]
            construction = 0
            for k in range(j+1, N):
                if world[k][i] == h:
                    construction += 1
                    ramp[k] = True
                else:
                    break
                if construction == L:
                    break
            if construction == L:
                continue
            else:
                break

        elif world[j][i] - world[j+1][i] == -1:
            h = world[j][i]
            construction = 0
            for k in range(j, -1, -1):
                if world[k][i] == h and not ramp[k]:
                    construction += 1
                    ramp[k] = True
                else:
                    break
                if construction == L:
                    break
            if construction == L:
                continue
            else:
                break

        else:
            break

print(result)