import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()
left = 0
right = n-1
tempLeft = 1000000000
tempRight = 1000000000
while left < right:
    if abs(array[left] + array[right]) < abs(tempLeft + tempRight):
        tempLeft = array[left]
        tempRight = array[right]
    if array[left] + array[right] >= 0:
        right -= 1
    else:
        left += 1

print(tempLeft, tempRight)