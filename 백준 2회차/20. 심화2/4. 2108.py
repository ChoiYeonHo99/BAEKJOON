import sys
import math

n = int(sys.stdin.readline().rstrip())
array = []
dictionary = {}
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    array.append(a)
    if a in dictionary:
        dictionary[a] += 1
    else:
        dictionary[a] = 1

array.sort()
print(round(sum(array) / n))
print(array[n//2])
sortedDictionary = sorted(dictionary.items(), key= lambda x : (-x[1],x[0]))
if len(sortedDictionary) > 1 and sortedDictionary[0][1] == sortedDictionary[1][1]:
    print(sortedDictionary[1][0])
else:
    print(sortedDictionary[0][0])
print(array[n-1] - array[0])