import sys

global count

def recursion(s: str, l: int, r: int):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s: str):
    return recursion(s, 0, len(s)-1)

t = int(sys.stdin.readline().rstrip())
for i in range(0, t):
    count = 0
    s = sys.stdin.readline().rstrip()
    print(isPalindrome(s), count)