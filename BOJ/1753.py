from sys import stdin
import heapq

v, e = map(int, stdin.readline().split())
graph = [[] for _ in range(v)]
least_cost_graph = [1e9] * v
start_node = int(stdin.readline()) - 1
least_cost_graph[start_node] = 0
queue = []
heapq.heappush(queue, [0, start_node])

for _ in range(e):
    u, v, w = map(int, stdin.readline().split())
    graph[u - 1].append([v - 1, w])

while queue:
    cost, node = heapq.heappop(queue)

    if cost < least_cost_graph[node]:
        continue

    for next_node, next_cost in graph[node]:
        if cost + next_cost < least_cost_graph[next_node]:
            least_cost_graph[next_node] = cost + next_cost
            heapq.heappush(queue, [least_cost_graph[next_node], next_node])

for result in least_cost_graph:
    if result == 1e9:
        print('INF')
    else:
        print(result)