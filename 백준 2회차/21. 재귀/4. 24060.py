import sys

def merge_sort(A: list, p: int, r: int):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p , q, r)

def merge(A: list, p: int, q: int, r: int):
    i, j, t = p, q + 1, 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = p, 0
    global count, result
    while i <= r:
        count += 1
        if count == k:
            result = tmp[t]
        A[i] = tmp[t]
        i += 1
        t += 1

n, k = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
result = 0
merge_sort(A, 0, n - 1)
if count >= k:
    print(result)
else:
    print(-1)