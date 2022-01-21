from sys import stdin
from collections import deque

node_num = int(stdin.readline())
edge_num = int(stdin.readline())

graph = [[] for _ in range(node_num)]
infection_graph = [False] * node_num

for _ in range(edge_num):
    start_node, end_node = map(int, stdin.readline().split())
    graph[start_node - 1].append(end_node - 1)
    graph[end_node - 1].append(start_node - 1)

queue = deque([0])
infection_graph[0] = True

while queue:
    node = queue.popleft()

    for next_node in graph[node]:
        if not infection_graph[next_node]:
            infection_graph[next_node] = True
            queue.append(next_node)

print(infection_graph.count(True) - 1)
