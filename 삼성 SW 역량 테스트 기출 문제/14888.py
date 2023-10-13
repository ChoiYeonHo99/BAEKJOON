import sys

n = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
operator_number = list(map(int, sys.stdin.readline().rstrip().split()))
global max, min
max = -1000000000
min = 1000000000
operator = []

def dfs():
    if len(operator) == n - 1:
        global max, min
        result = sequence[0]
        for i in range(n-1):
            if operator[i] == "+":
                result += sequence[i+1]
            if operator[i] == "-":
                result -= sequence[i+1]
            if operator[i] == "x":
                result *= sequence[i+1]
            if operator[i] == "%":
                if result < 0:
                    result *= -1
                    result //= sequence[i+1]
                    result *= -1
                else:
                    result //= sequence[i+1]
        if result > max:
            max = result
        if result < min:
            min = result
        return
    if operator_number[0] > 0:
        operator_number[0] -= 1
        operator.append("+")
        dfs()
        operator.pop()
        operator_number[0] += 1
    if operator_number[1] > 0:
        operator_number[1] -= 1
        operator.append("-")
        dfs()
        operator.pop()
        operator_number[1] += 1
    if operator_number[2] > 0:
        operator_number[2] -= 1
        operator.append("x")
        dfs()
        operator.pop()
        operator_number[2] += 1
    if operator_number[3] > 0:
        operator_number[3] -= 1
        operator.append("%")
        dfs()
        operator.pop()
        operator_number[3] += 1

dfs()
print(max)
print(min)