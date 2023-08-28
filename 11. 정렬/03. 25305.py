import sys

nk = sys.stdin.readline().rstrip().split()
n = int(nk[0])
k = int(nk[1])
score_str = sys.stdin.readline().rstrip().split()
score_int = []

for i in range(0, n):
    score_int.append(int(score_str[i]))

score_int.sort(reverse=True)
print(score_int[k-1])