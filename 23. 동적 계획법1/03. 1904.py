import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    tile = [1] * (n + 1)
    tile[2] = 2
    for i in range(3, n+1):
        tile[i] = (tile[i-1] + tile[i-2]) % 15746
    print(tile[n])