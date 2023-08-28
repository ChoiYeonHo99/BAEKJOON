import sys

def search(n: int, left: int, right: int):
    if left > right:
        return False
    mid = (left + right) // 2
    if n_list[mid] == n:
        return True
    else:
        if n_list[mid] > n:
            return search(n, left, mid-1)
        else:
            return search(n, mid+1, right)

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
n_list.sort()
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(m):
    if search(m_list[i], 0, n-1):
        print(1)
    else:
        print(0)