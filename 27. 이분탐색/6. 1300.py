import sys

def count(num: int):
    count = 0
    for row in range(1, n+1):
        count += min((num-1) // row, n)
    return count


def search(left: int, right: int):
    global result
    result = right
    if left > right:
        return
    mid = (left + right) // 2
    if count(mid) < k:
        return search(mid+1, right)
    else:
        return search(left, mid-1)

result = 0
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

search(0, n*n)
print(result)