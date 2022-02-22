from sys import stdin

n = int(stdin.readline())
graph = [0] * 1001
max_x = 0
max_y = 0
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    graph[x - 1] = y

index = graph.index(max_y)  # 최댓값의 인덱스
check = 0
result = 0

# 최댓값의 인덱스까지
for i in range(index):
    check = max(check, graph[i])  # 최대 높이가 변하면 갱신
    result += check  # 최대 높이 만큼 더해주기
check = 0

# 끝에서 최대값의 인덱스 까지
for i in range(max_x, index, -1):
    check = max(check, graph[i])  # 최대 높이가 변하면 갱신
    result += check  # 최대 높이 만큼 더해주기

print(result + max_y)  # 결과값 + 최대높이
