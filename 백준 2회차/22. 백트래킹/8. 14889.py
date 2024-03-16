import sys

def calculation():
    if len(start) != len(link):
        return

    s = 0
    l = 0
    for i in range(len(start)):
        for j in range(i+1, len(start)):
            s += ability[start[i]][start[j]] + ability[start[j]][start[i]]
            l += ability[link[i]][link[j]] + ability[link[j]][link[i]]
    
    global result
    result = min(result, abs(s - l))

def member(index: int):
    if index >= n:
        calculation()
        return

    start.append(index)
    member(index+1)
    start.pop()

    link.append(index)
    member(index+1)
    link.pop()

n = int(sys.stdin.readline().rstrip())
ability = []
result = float('inf')
start = []
link = []
for _ in range(n):
    ability.append(list(map(int, sys.stdin.readline().rstrip().split())))

member(0)
print(result)