import sys

s = sys.stdin.readline().rstrip()
s_set = set([])

for i in range(0, len(s)):
    for j in range(0, len(s) - i):
        s_set.add(s[j : j+1+i])

print(len(s_set))