from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
ladder = [False for _ in range(101)]
snake = [False for _ in range(101)]
graph = [0 for _ in range(101)]
visit_graph = [False for _ in range(101)]

# 사다리 추가
for _ in range(n):
    a, b = map(int ,stdin.readline().split())
    ladder[a] = b

# 뱀 추가
for _ in range(m):
    a, b = map(int ,stdin.readline().split())
    snake[a] = b

queue = deque()
queue.append(1)
visit_graph[1] = True

while queue:
    start = queue.popleft()
    
    for dice in range(1, 7):
        current = start + dice
    
        if 1 <= current <= 100 and not visit_graph[current]:
            if ladder[current]:
                current = ladder[current]

            if snake[current]:
                current = snake[current]
            
            if not visit_graph[current]:
                queue.append(current)
                visit_graph[current] = True
                graph[current] = graph[start] + 1

print(graph[100])
