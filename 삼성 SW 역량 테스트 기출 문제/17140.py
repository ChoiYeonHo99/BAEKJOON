import sys

r, c, k = map(int, sys.stdin.readline().split())
A = []
for _ in range(3):
    A.append(list(map(int, sys.stdin.readline().split())))

possible = False
for t in range(101):
    try:
        if A[r-1][c-1] == k:
            print(t)
            possible = True
            break
    except:
        a = 1

    if len(A) >= len(A[0]):
        for i in range(len(A)):
            dic = {}
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    continue
                if A[i][j] in dic:
                    dic[A[i][j]] += 1
                else:
                    dic[A[i][j]] = 1
            dic = sorted(dic.items(), key = lambda item: (item[1], item[0]))
            A[i].clear()
            for x in dic:
                A[i].append(x[0])
                A[i].append(x[1])
        
        maxLength = len(A[0])
        for i in range(len(A)):
            if len(A[i]) > maxLength:
                maxLength = len(A[i])
        
        for i in range(len(A)):
            for j in range(maxLength - len(A[i])):
                A[i].append(0)
    else:
        change = []
        maxLength = 0
        for i in range(len(A[0])):
            dic = {}
            for j in range(len(A)):
                if A[j][i] == 0:
                    continue
                if A[j][i] in dic:
                    dic[A[j][i]] += 1
                else:
                    dic[A[j][i]] = 1
            dic = sorted(dic.items(), key = lambda item: (item[1], item[0]))
            temp = []
            for x in dic:
                temp.append(x[0])
                temp.append(x[1])
            change.append(temp)
            if len(temp) > maxLength:
                maxLength = len(temp)
        
        A = [[0] * len(change) for _ in range(maxLength)]
        for i in range(len(change)):
            for j in range(len(change[i])):
                A[j][i] = change[i][j]

if not possible:
    print(-1)