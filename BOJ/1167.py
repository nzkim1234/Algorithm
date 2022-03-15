import queue
from sys import stdin
from collections import deque
from unittest import result
v = int(stdin.readline())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    tree = list(map(int, stdin.readline().split()))
    tree.pop()
    node = tree[0]

    for i in range(1, (len(tree) - 1), 2):
        graph[node].append([tree[i], tree[i + 1]])

result = 0
for i in range(1, v + 1):
    queue = deque()
    
    for j in graph[i]:
        queue.append(j + [0])

    visit_graph = [0] * (v + 1)
    visit_graph[i] = 1
    
    while queue:
        node, value, current_result = queue.popleft()
        
        if not visit_graph[node]:
            visit_graph[node] = 1
            
            for j in graph[node]:
                queue.append(j + [current_result + value])

    result = max(result, current_result)

print(result)
