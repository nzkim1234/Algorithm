from collections import deque

n = int(input())
graph = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
q = deque([[1, 0]])
graph[1][0] = 0

while q:
    s, c = q.popleft()

    # 복사하는 연산
    if graph[s][s] == -1:
        graph[s][s] = graph[s][c] + 1
        q.append([s, s])

    # 복사한 것을 붙여넣는 연산
    if s + c <= n and graph[s + c][c] == -1:
        graph[s + c][c] = graph[s][c] + 1
        q.append([s + c, c])

    # 하나 뺴는 연산
    if s - 1 >= 0 and graph[s-1][c] == -1:
        graph[s - 1][c] = graph[s][c] + 1
        q.append([s - 1, c])

result = -1

for i in range(n + 1):
    if graph[n][i] != -1:
        if result == -1 or result > graph[n][i]:
            result = graph[n][i]

print(result)
