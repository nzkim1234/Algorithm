from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    s, e, v = map(int ,stdin.readline().split())
    graph[s]. append([e, v])
    graph[e]. append([s, v])

v1, v2 = map(int, stdin.readline().split())
visit_graph = [1e9] * (n + 1)
queue = []
heapq.heappush(queue, [0, 1, [False, False]])
visit_graph[1] = 0

while queue:
    value, node, visited_node = heapq.heappop(queue)
    print(node, value)
    print(queue)
    for next_node, next_value in graph[node]:
        print(visit_graph)
        if visit_graph[next_node] > value + next_value:
            if next_node == v1:
                visited_node[0] = True
            elif next_node == v2:
                visited_node[1] = True
            
            visit_graph[next_node] = value + next_value
            heapq.heappush(queue, [next_value, next_node, visited_node])
    
        