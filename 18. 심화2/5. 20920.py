import sys

nm = list(map(int, sys.stdin.readline().rstrip().split()))
n = nm[0]
m = nm[1]
dictionary = {}

for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1

sortedDictionary = sorted(dictionary.items(),key= lambda x : (-x[1],-len(x[0]),x[0]))  

for i in sortedDictionary:
    print(i[0])