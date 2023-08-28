import sys

def solution():
    global sum_board
    result = k ** 2
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            temp = sum_board[i + k - 1][j + k - 1] - sum_board[i - 1][j + k - 1] - sum_board[i + k - 1][j - 1] + sum_board[i - 1][j - 1]
            result = min(result, temp, k ** 2 - temp)
    return result

n, m, k = map(int, sys.stdin.readline().rstrip().split())
color = ['B', 'W']
sum_board = [[0]*(m+1)]
for i in range(1, n+1):
    temp = sys.stdin.readline().rstrip()
    sum_board.append(sum_board[0][:])
    for j in range(1, m+1):
        num = 0
        if temp[j-1] == color[(abs(i-j-2))%2]:
            num = 1
        sum_board[i][j] = (sum_board[i-1][j] + sum_board[i][j-1] - sum_board[i-1][j-1]) + num

print(solution())