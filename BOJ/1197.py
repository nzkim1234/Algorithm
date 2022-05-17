from sys import stdin
import heapq

v, e = map(int, stdin.readline().split())
graph = [[] for _ in range(v + 1)]
visit_graph = [False] * (v + 1)
result = 0

# 노드 추가
for i in range(e):
    a, b, c = map(int ,stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

queue = [[0, 1]]

# 힙을 이용해 최소값으로 탐색하기
while queue:
    node = heapq.heappop(queue)
    
    if not visit_graph[node[1]]:
        visit_graph[node[1]] = True
        result += node[0]
    
        for next in graph[node[1]]:
            heapq.heappush(queue, next)

print(result)
