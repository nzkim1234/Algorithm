from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, v = map(int, stdin.readline().split())
    graph[s].append([e, v])

start, end = map(int, stdin.readline().split())

visit_graph = [1e9] * (n + 1)
bus_path = [[] for _ in range(n + 1)]
queue = [[0, start, [start]]]
visit_graph[start] = 0

while queue:
    value, node, path = heapq.heappop(queue)

    if value > visit_graph[node]:
        continue
    
    for e, v in graph[node]:
        if value + v < visit_graph[e]:
            v += value
            visit_graph[e] = v
            bus_path[e] = path + [e]
            heapq.heappush(queue, [ v, e, path + [e]])

print(visit_graph[end])
print(len(bus_path[end]))
print(*bus_path[end])