import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

array.sort()
left = 0
right = n-1
count = 0
while left < right:
    if array[left] + array[right] == x:
        count += 1

    if array[left] + array[right] >= x:
        right -= 1
    else:
        left += 1

print(count)