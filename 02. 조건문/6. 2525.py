x = input().split(" ")
h = int(x[0])
m = int(x[1])
y = int(input())

result_m = (m + y) % 60
plus_h = (m + y) // 60
result_h = (h + plus_h) % 24

print(result_h, result_m)