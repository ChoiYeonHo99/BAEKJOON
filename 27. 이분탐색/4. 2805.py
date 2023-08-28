import sys

def cut(height: int):
    size = 0
    for i in tree:
        if i - height > 0:
            size += i - height
    return size

def search(left: int, right: int):
    global max_height
    if left > right:
        return
    mid = (left + right) // 2
    if cut(mid) >= m:
        if max_height < mid:
            max_height = mid
            return search(mid+1, right)
        else:
            return
    else:
        return search(left, mid-1)

n, m = map(int, sys.stdin.readline().rstrip().split())
max_height = 0
tree = list(map(int, sys.stdin.readline().rstrip().split()))
search(1, max(tree))
print(max_height)