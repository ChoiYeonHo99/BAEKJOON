import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
sum_list = [0] * (n+1)
m_list = [0] * m

for i in range(n):
    sum_list[i+1] = sum_list[i] + num_list[i]
    m_list[sum_list[i+1] % m] += 1

count = m_list[0]
for i in range(m):
    if m_list[i] >= 2:
        count += m_list[i] * (m_list[i]-1) / 2
print(int(count))