from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    s, e, v = map(int ,stdin.readline().split())
    graph[s]. append([e, v])
    graph[e]. append([s, v])

v1, v2 = map(int, stdin.readline().split())
value_graph = [1e9] * (n + 1)
visit_graph = [False] * (n + 1)
queue = []
result = 0
heapq.heappush(queue, [0, v1, visit_graph])
value_graph[v1] = 0
visit_graph[v1] = True

while queue:
    value, node, visit_graph = heapq.heappop(queue)

    for next_node, next_value in graph[node]:
        if value_graph[next_node] > next_value + value:
            value_graph[next_node] = next_value + value
            visit_graph[next_node] = True
            heapq.heappush(queue, [next_value, next_node, visit_graph])

print(visit_graph, value_graph)