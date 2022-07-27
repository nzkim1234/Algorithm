from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, v = map(int, stdin.readline().split())
    graph[s].append([e, v])

start, end = map(int, stdin.readline().split())

visit_graph = [1e9] * (n + 1)  # 최소비용 저장
bus_path = [[] for _ in range(n + 1)]  # 들렸던 경로 저장
queue = []
heapq.heappush(queue, [0, start, [start]])  # [최소비용, 현재노드, 지금까지 들렸던 경로]
visit_graph[start] = 0

while queue:
    value, node, path = heapq.heappop(queue)

    if value > visit_graph[node]:
        continue
    
    # 다음 노드의 비용이 현재 최소 비용 + 다음노드의 비용 보다 크면 최소 비용 갱신
    for e, v in graph[node]:
        if value + v < visit_graph[e]:
            visit_graph[e] = v + value
            bus_path[e] = path + [e]
            heapq.heappush(queue, [v + value, e, path + [e]])

print(visit_graph[end])
print(len(bus_path[end]))
print(*bus_path[end])
