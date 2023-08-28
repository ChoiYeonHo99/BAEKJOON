import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
start = 0
end = 0
sum = 0
minLength = 100000

while end < N:
    if sum <= S:
        sum += array[end]
        end += 1
    else:
        sum -= array[start]
        start +=1
    
    if sum >= S and end - start < minLength:
        minLength = end - start

while start < N:
    sum -= array[start]
    start +=1
    
    if sum >= S and end - start < minLength:
        minLength = end - start


if minLength == 100000:
    print(0)
else:
    print(minLength)