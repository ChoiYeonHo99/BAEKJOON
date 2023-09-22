import sys
import itertools
from bisect import bisect_right

N, C = map(int, sys.stdin.readline().rstrip().split())
objects = list(map(int, sys.stdin.readline().rstrip().split()))

left_objects = objects[:N//2]
right_objects = objects[N//2:]

subset_left = []
subset_right = []

for num in range(len(left_objects) + 1):
    for sub_set in itertools.combinations(left_objects, num):
        subset_left.append(sum(sub_set))

for num in range(len(right_objects) + 1):
    for sub_set in itertools.combinations(right_objects, num):
        subset_right.append(sum(sub_set))

subset_left.sort()
count = 0
for i in range(len(subset_right)):
    if subset_right[i] > C:
        continue
    elif subset_right[i] == C:
        count += 1
        continue

    index = bisect_right(subset_left, C - subset_right[i])
    count += index

print(count)