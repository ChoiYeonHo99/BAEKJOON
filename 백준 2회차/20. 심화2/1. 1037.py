import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
print(max(array) * min(array))