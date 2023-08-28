import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
size = n
queue = [i for i in range(1, n+1)]
delete = k-1
result = []

while size > 0:
    delete = delete % size
    result.append(str(queue[delete]))
    del queue[delete]
    size -= 1
    delete += k - 1

print("<", ", ".join(result), ">", sep = '')