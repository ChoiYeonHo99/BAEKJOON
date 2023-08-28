import sys

n = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().rstrip().split()))
people.sort()
time = 0
result = 0

for i in range(n):
    time += people[i]
    result += time

print(result)