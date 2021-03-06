from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
visit_graph = [0] * (n + 1)

# 그래프 생성
for i in range(1, n + 1):
    line = list(map(int, stdin.readline().split()))

    for j in range(len(line)):
        if line[j] == 1:
            graph[i].append(j + 1)

plan = list(map(int, stdin.readline().split()))  # 여행 계획

# bfs 탐색
start = plan[0]
queue = deque([start])
visit_graph[start] = 1

while queue:
    x = queue.popleft()

    for next in graph[x]:
        if visit_graph[next] == 0:
            visit_graph[next] += 1
            queue.append(next)

success = True

# 여행계획의 도시를 방문하지 않았다면 success = false, break
for city in plan:
    if visit_graph[city] == 0:
        success = False
        break

if success:
    print('YES')
else:
    print('NO')
