import queue
from sys import stdin
from collections import deque

n = int(stdin.readline())
tree = [[] for _ in range(n + 1)]


for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


visit_graph = [-1] * (n + 1)
visit_graph[1] = 0
queue = deque()
queue.append(1)

# 하나의 노드에서부터 탐색
while queue:
    before_node = queue.popleft()
    for node, value in tree[before_node]:
        if visit_graph[node] == -1 and visit_graph[node] != 0:
            visit_graph[node] = visit_graph[before_node] + value
            queue.append(node)

# 값이 최대인 노드를 찾고 그 노드부터 다시 한번 탐색
index = visit_graph.index(max(visit_graph))
visit_graph = [-1] * (n + 1)
visit_graph[index] = 0
queue = deque()
queue.append(index)

while queue:    
    before_node = queue.popleft()
    for node, value in tree[before_node]:
        if visit_graph[node] == -1 and visit_graph[node] != 0:
            visit_graph[node] = visit_graph[before_node] + value
            queue.append(node)

print(max(visit_graph))
