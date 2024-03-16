import sys

def between():
    if len(operator) == n - 1:
        global maxValue, minValue
        result = array[0]
        for i in range(n-1):
            if operator[i] == "+":
                result += array[i+1]
            if operator[i] == "-":
                result -= array[i+1]
            if operator[i] == "x":
                result *= array[i+1]
            if operator[i] == "%":
                if result < 0:
                    result *= -1
                    result //= array[i+1]
                    result *= -1
                else:
                    result //= array[i+1]
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        return
    
    if operator_tmp[0] > 0:
        operator_tmp[0] -= 1
        operator.append("+")
        between()
        operator.pop()
        operator_tmp[0] += 1
    if operator_tmp[1] > 0:
        operator_tmp[1] -= 1
        operator.append("-")
        between()
        operator.pop()
        operator_tmp[1] += 1
    if operator_tmp[2] > 0:
        operator_tmp[2] -= 1
        operator.append("x")
        between()
        operator.pop()
        operator_tmp[2] += 1
    if operator_tmp[3] > 0:
        operator_tmp[3] -= 1
        operator.append("%")
        between()
        operator.pop()
        operator_tmp[3] += 1

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
operator_tmp = list(map(int, sys.stdin.readline().rstrip().split()))
operator = []
maxValue = -1000000000
minValue = 1000000000

between()
print(maxValue)
print(minValue)