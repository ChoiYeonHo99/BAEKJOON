import sys

def merge_sort(A: list):
    if len(A) == 1:
        return A
    mid = (len(A) + 1) // 2
    leftA = merge_sort(A[:mid])
    rightA = merge_sort(A[mid:])

    tmp = []
    i = 0
    j = 0

    global count, k
    
    while i < len(leftA) and j < len(rightA):
        if leftA[i] < rightA[j]:
            tmp.append(leftA[i])
            count += 1
            if count == k:
                print(leftA[i])
            i += 1
        else:
            tmp.append(rightA[j])
            count += 1
            if count == k:
                print(rightA[j])
            j += 1
    
    while i < len(leftA):
        tmp.append(leftA[i])
        count += 1
        if count == k:
            print(leftA[i])
        i += 1
        
    while j < len(rightA):
        tmp.append(rightA[j])
        count += 1
        if count == k:
            print(rightA[j])
        j += 1

    return tmp

global count, k
count = 0
nk = list(map(int, sys.stdin.readline().strip().split()))
n = nk[0]
k = nk[1]
a = list(map(int, sys.stdin.readline().strip().split()))
a = merge_sort(a)
if count < k:
    print(-1)