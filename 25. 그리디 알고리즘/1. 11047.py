import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

count = 0
for i in range(n-1, -1, -1):
    if coin[i] <= k:
        count += k // coin[i]
        k = k % coin[i]
    if k == 0:
        break

print(count)