from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
visit_graph = [[1e9, [], 0] for _ in range(n + 1)]

for b in range(1, m + 1):
    s, e, v = map(int, stdin.readline().split())
    graph[s].append([b, e, v])

start, end = map(int, stdin.readline().split())

queue = []
visit_graph[start][0] = 0
visit_graph[start][1] = [1]
visit_graph[start][2] = 1
heapq.heappush(queue, [0, start])

while queue:
    value, node= heapq.heappop(queue)

    for b, e, v in graph[node]:
        if visit_graph[e][0] > value + v:
            visit_graph[e][0] = value + v
            visit_graph[e][1] = visit_graph[node][1] + [e]
            visit_graph[e][2] = visit_graph[node][2] + 1
            heapq.heappush(queue, [value + v, e])

print(visit_graph[end][0])
print(visit_graph[end][2])
print(*visit_graph[end][1])