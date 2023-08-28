import sys

expression = sys.stdin.readline().rstrip()
numbers_str = expression.replace('+', '-').split('-')
numbers = []
for i in range(len(numbers_str)):
    numbers.append(int(numbers_str[i]))
operators = [operator for operator in expression if operator in '+-']

minus = False
result = numbers[0]
for i in range(1, len(numbers)):
    if operators[i-1] == "-":
        minus = True
    if minus:
        result -= numbers[i]
    else:
        result += numbers[i]

print(result)