import sys

s = sys.stdin.readline().rstrip()
p = int(sys.stdin.readline().rstrip())
alphabet = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(26):
        alphabet[i][j] = alphabet[i - 1][j]
    alphabet[i][ord(s[i - 1]) - 97] += 1

for _ in range(p):
    a, l, r = sys.stdin.readline().rstrip().split()
    asc = ord(a) - 97
    if int(l) == 0:
        print(alphabet[int(r)+1][asc])
    else:
        print(alphabet[int(r)+1][asc] - alphabet[int(l)][asc])