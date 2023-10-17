import sys

def run():
    for i in range(1, N+1):
        u = i
        for j in range(1, H+1):
            u += ladder[j][u]
        if u != i:
            return False
    return True

def search(count: int):
    for k in range(2):
        if k == 1 and count == 3:
            return False

        for i in range(1, N):
            for j in range(1, H+1):
                if ladder[j][i] == 0 and ladder[j][i+1] == 0:
                    ladder[j][i] = 1
                    ladder[j][i+1] = -1

                    if k == 1:
                        subsequently = search(count+1)
                        if subsequently:
                            return True

                    if run():
                        print(count)
                        return True
                    else:
                        ladder[j][i] = 0
                        ladder[j][i+1] = 0

    return False

N, M, H = map(int, sys.stdin.readline().split())
ladder = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a][b] = 1
    ladder[a][b+1] = -1

if run():
    print(0)
else:
    possible = search(1)
    if not possible:
        print(-1)