import sys

nm = list(map(int, sys.stdin.readline().rstrip().split()))
n = nm[0]
m = nm[1]

sequence = []

def dfs():
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n+1):
        if i not in sequence:
            if len(sequence) == 0:
                sequence.append(i)
                dfs()
                sequence.pop()
            else:
                if sequence[len(sequence)-1] < i:
                    sequence.append(i)
                    dfs()
                    sequence.pop()

dfs()