import sys

n = int(sys.stdin.readline().rstrip())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
fare = list(map(int, sys.stdin.readline().rstrip().split()))

min = fare[0]
result = distance[0] * min
for i in range(1, n-1):
    if min > fare[i]:
        min = fare[i]
    result += distance[i] * min
    
print(result)