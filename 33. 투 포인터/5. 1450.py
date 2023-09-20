import sys
import math
import itertools

N, C = map(int, sys.stdin.readline().rstrip().split())
objects = list(map(int, sys.stdin.readline().rstrip().split()))

left_objects = objects[:math.ceil(N/2)]
right_objects = objects[math.ceil(N/2):]

subset_left = []
subset_right = []

for num in range(len(left_objects) + 1):
    for sub_set in itertools.combinations(left_objects, num):
        subset_left.append(sum(sub_set))

for num in range(len(right_objects) + 1):
    for sub_set in itertools.combinations(right_objects, num):
        subset_right.append(sum(sub_set))

subset_left.sort()