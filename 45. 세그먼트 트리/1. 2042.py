import sys
import math

N, M, K = map(int, sys.stdin.readline().split())
h = math.ceil(math.log2(N))
tree = [0] * 2**(h+1)

for i in range(N):
    tree[2**h+i] = int(sys.stdin.readline())
for i in range(2**h-1, -1, -1):
    tree[i] = tree[i*2] + tree[i*2+1]

for _ in range(M+K) :
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        index = 2**h + b - 1
        diff = c - tree[index]
        while index >= 1:
            tree[index] += diff
            index //= 2

    else:
        start = 2**h + b - 1
        end = 2**h + c - 1
        result = 0
        while start <= end:
            if start == end:
                result += tree[start]
                break

            if start % 2 == 1:
                result += tree[start]
                start = (start+1) // 2
            else:
                start //= 2

            if end % 2 == 0:
                result += tree[end]
                end = (end-1) // 2
            else:
                end //= 2

        print(result)