import sys

while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    divisor = []
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor.append(i)
            sum += i
    if sum == n:
        divisior_Str = str(n) + " = 1"
        for i in range(1, len(divisor)):
            divisior_Str += " + " + str(divisor[i])
        print(divisior_Str)
    else:
        print(str(n) + " is NOT perfect.")