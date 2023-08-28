import sys

def cut(size: int):
    count = 0
    for i in k_list:
        count += i // size
    return count

def search(left: int, right: int):
    global max_size
    if left > right:
        return
    mid = (left + right) // 2
    if cut(mid) >= n:
        if max_size < mid:
            max_size = mid
            return search(mid+1, right)
        else:
            return
    else:
        return search(left, mid-1)

k, n = map(int, sys.stdin.readline().rstrip().split())
max_size = 0
k_list = []
for _ in range(k):
    k_list.append(int(sys.stdin.readline().rstrip()))
search(1, max(k_list))
print(max_size)