from sys import stdin
from collections import deque
n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(n - 1):
    s, e, v = map(int, stdin.readline().split())
    graph[s].append([e, v])
    graph[e].append([s, v])

for _ in range(m):
    s, e = map(int, input().split())
    queue = deque()
    queue.append(s)
    visit_graph = [-1] * (n + 1)
    visit_graph[s] = 0

    while queue:
        destination = queue.popleft()

        if destination == e:
            break

        for next_node, value in graph[destination]:
            if visit_graph[next_node] == -1:
                visit_graph[next_node] = visit_graph[destination] + value
                queue.append(next_node)

    print(visit_graph[e])