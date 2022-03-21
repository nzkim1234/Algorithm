from sys import stdin
from collections import deque

# 트리의 지름을 찾는방법 = 임의의 점에서부터 제일 거리가 먼 노드를 찾은 후 다시 그 노드에서부터 구한 최대거리값이 트리의 지름이다.

v = int(stdin.readline())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    tree = list(map(int, stdin.readline().split()))
    tree.pop()
    node = tree[0]

    for i in range(1, (len(tree) - 1), 2):
        graph[node].append([tree[i], tree[i + 1]])

# 임의의 노드에서 제일 거리가 긴 노드 찾기

visit_graph = [-1] * (v + 1)
queue = deque()
queue.append(1)
visit_graph[1] = 0

while queue:    
    before_node = queue.popleft()
    for node, value in graph[before_node]:
        if visit_graph[node] == -1 and visit_graph[node] != 0:
            visit_graph[node] = visit_graph[before_node] + value
            queue.append(node)

index = visit_graph.index(max(visit_graph))  # 찾은 노드

# 다시 한번 제일 먼 거리 찾기
queue = deque()
queue.append(index)
visit_graph = [-1] * (v + 1)
visit_graph[index] = 0

while queue:    
    before_node = queue.popleft()
    for node, value in graph[before_node]:
        if visit_graph[node] == -1 and visit_graph[node] != 0:
            visit_graph[node] = visit_graph[before_node] + value
            queue.append(node)
            
print(max(visit_graph))  # 트리의 지름
