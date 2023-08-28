import sys

n = int(sys.stdin.readline().rstrip())
stat = []
link = []
start = []
global min
min = 100 * n

for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    stat.append(line)

def dfs(s: int):
    if len(link) == (n // 2):
        global min
        full = [i for i in range(n)]
        start = [x for x in full if x not in link]
        link_team = 0
        start_team = 0
        for i in range(n//2):
            for j in range(i, n//2):
                link_team += stat[link[i]][link[j]]
                link_team += stat[link[j]][link[i]]
        for i in range(n//2):
            for j in range(i, n//2):
                start_team += stat[start[i]][start[j]]
                start_team += stat[start[j]][start[i]]
        if abs(link_team - start_team) < min:
            min = abs(link_team - start_team)
    for i in range(s, n):
        link.append(i)
        dfs(i+1)
        link.pop()

dfs(0)
print(min)