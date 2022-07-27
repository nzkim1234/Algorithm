from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    s, e, v = map(int ,stdin.readline().split())
    graph[s]. append([e, v])
    graph[e]. append([s, v])

v1, v2 = map(int, stdin.readline().split())

# 다익스트라 탐색
def calc(start):
    visit_graph = [1e9] * (n + 1)
    visit_graph[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        value, node = heapq.heappop(queue)

        for next_node, next_value in graph[node]:
            sum_value = value + next_value

            if visit_graph[next_node] > sum_value:
                visit_graph[next_node] = sum_value
                heapq.heappush(queue, [sum_value, next_node])
    
    return visit_graph

first = calc(1)  # 첫 노드에서 최소값
result_v1 = calc(v1)  # v1 노드에서의 최소값 
result_v2 = calc(v2)  # v2 노드에서의 최소값

# 1 -> v1 -> v2 -> n or 1 -> v2 -> v1 -> n
result = min(first[v1] + result_v1[v2] + result_v2[n], first[v2] + result_v1[n] + result_v2[v1])

if result < 1e9:
    print(result)
else:
    print(-1)
