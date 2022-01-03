import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = []
m_list = []
for i in range(n):
    n_list.append(input().strip())
for i in range(m):
    m_list.append(input().strip())
result = list(set(n_list) & set(m_list))
result.sort()
print(len(result))
for i in result:
    print(i)
