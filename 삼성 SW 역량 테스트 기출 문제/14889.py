import sys

def calculation(start, link):
    if len(start) != len(link):
        return
    
    start_ability = 0
    link_ability = 0
    for i in range(len(start)):
        for j in range(i+1, len(start)):
            start_ability += ability[start[i]][start[j]] + ability[start[j]][start[i]]
            link_ability += ability[link[i]][link[j]] + ability[link[j]][link[i]]
    
    global result
    result = min(result, abs(start_ability - link_ability))

def member(i: int, start, link):
    if i >= N:
        calculation(start, link)
        return

    member(i+1, start+[i], link)
    member(i+1, start, link+[i])

N = int(sys.stdin.readline().rstrip())
ability = []
result = float('inf')
for _ in range(N):
    ability.append(list(map(int, sys.stdin.readline().rstrip().split())))

member(0, [], [])
print(result)