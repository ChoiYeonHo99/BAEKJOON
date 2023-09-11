import sys
from collections import deque

def bfs(s: int, e: int):
    dp = [10000] * 10000
    dp[s] = 0
    qn = deque([s])
    qd = deque([0])
    qp = deque([""])

    while qn:
        n = qn.popleft()
        d = qd.popleft()
        p = qp.popleft()
        if n == e:
            print(p)
            break

        if d + 1 < dp[D(n)]:
            dp[D(n)] = d + 1
            qn.append(D(n))
            qd.append(d+1)
            qp.append(p + "D")
        if d + 1 < dp[S(n)]:
            dp[S(n)] = d + 1
            qn.append(S(n))
            qd.append(d+1)
            qp.append(p + "S")
        if d + 1 < dp[L(n)]:
            dp[L(n)] = d + 1
            qn.append(L(n))
            qd.append(d+1)
            qp.append(p + "L")
        if d + 1 < dp[R(n)]:
            dp[R(n)] = d + 1
            qn.append(R(n))
            qd.append(d+1)
            qp.append(p + "R")

def D(n: int):
    return n * 2 % 10000

def S(n: int):
    if n == 0:
        return 9999
    return n - 1

def L(n: int):
    a0 = n // 1000
    n = n - 1000 * a0
    a1 = n // 100
    n = n - 100 * a1
    a2 = n // 10
    n = n - 10 * a2
    a3 = n
    result = 0
    result += a0
    result += 1000 * a1
    result += 100 * a2
    result += 10 * a3
    return result

def R(n: int):
    a0 = n // 1000
    n = n - 1000 * a0
    a1 = n // 100
    n = n - 100 * a1
    a2 = n // 10
    n = n - 10 * a2
    a3 = n
    result = 0
    result += 100 * a0
    result += 10 * a1
    result += a2
    result += 1000 * a3
    return result

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    bfs(A, B)