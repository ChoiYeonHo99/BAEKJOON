import sys

def installation(distance: int):
    last_installation = 0
    remaining_Modem = c - 1
    for i in range(1, n):
        if houses[i] - houses[last_installation] >= distance:
            last_installation = i
            remaining_Modem -= 1
    if remaining_Modem <= 0:
        return True
    return False

def search(left: int, right: int):
    global max_distance
    if left > right:
        return
    mid = (left + right) // 2
    if installation(mid):
        max_distance = mid
        return search(mid+1, right)
    else:
        return search(left, mid-1)

n, c = map(int, sys.stdin.readline().rstrip().split())
max_distance = 0
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline().rstrip()))
houses.sort()
search(0, houses[n-1])
print(max_distance)