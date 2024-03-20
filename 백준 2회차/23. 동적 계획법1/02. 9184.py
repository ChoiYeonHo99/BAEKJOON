import sys

def w(a: int, b: int, c: int):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    s = str(a) + ", " + str(b) + ", " + str(c)
    if s in dic:
        return dic[s]

    if a < b and b < c:
        v = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        dic[s] = v
        return v

    v = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    dic[s] = v
    return v

dic = {}
while 1:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1:
        break

    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(w(a, b, c)))