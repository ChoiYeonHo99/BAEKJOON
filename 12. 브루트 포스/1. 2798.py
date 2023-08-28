import sys

nm = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))
n = nm[0]
m = nm[1]

min = m
sum = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if m - cards[i] - cards[j] - cards[k] < min and m - cards[i] - cards[j] - cards[k] >= 0:
                sum = cards[i] + cards[j] + cards[k]
                min = m - cards[i] - cards[j] - cards[k]

print(sum)