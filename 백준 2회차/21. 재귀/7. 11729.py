import sys

def hanoi(n, start, end, mid):
    global count
    if n == 1:
        count += 1
        record.append((start, end))
        return
    
    hanoi(n-1, start, mid, end)
    count += 1
    record.append((start, end))
    hanoi(n-1, mid, end, start)

global count, record
count = 0
record = []

n = int(sys.stdin.readline().strip())
hanoi(n, 1, 3, 2)
print(count)
for i in range(0, count):
    print(record[i][0], record[i][1])