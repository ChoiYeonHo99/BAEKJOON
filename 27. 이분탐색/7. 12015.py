import sys

def search(target: int, left: int, right: int):
    if left > right:
        return left
    mid = (left + right) // 2
    if result[mid] < target:
        return search(target, mid+1, right)
    else:
        return search(target, left, mid-1)
    
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
result = [0]

for i in a:
    if result[-1] < i:
        result.append(i)
    else:
        result[search(i, 0, len(result) - 1)] = i

print(len(result) - 1)