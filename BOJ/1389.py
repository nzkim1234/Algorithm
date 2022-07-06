from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
people = [[] for _ in range(n + 1)]
result_num = 1e9
result = 0

# 입력 받기
for _ in range(m):
    a, b = map(int,stdin.readline().split())
    people[a].append(b)
    people[b].append(a)


for i in range(1, n + 1, 1):
    visit_graph = [False] * (n + 1)  # 방문 여부
    num_graph = [0] * (n + 1)  # 좌표의 값
    queue = deque()
    visit_graph[i] = True
    queue.append(i)
    
    # bfs 탐색
    while queue:
        current_num = queue.popleft()
    
        for next_num in people[current_num]:
            if not visit_graph[next_num]:
                num_graph[next_num] = num_graph[current_num] + 1
                queue.append(next_num)
                visit_graph[next_num] = True
    
    # 결과 계산
    if sum(num_graph) < result_num:
        result_num = sum(num_graph)
        result = i

print(result)
