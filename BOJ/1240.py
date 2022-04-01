from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    s, e, v = map(int, stdin.readline().split())
    graph[s - 1].append([e - 1, v])
    graph[e - 1].append([s - 1, v])

for _ in range(m):
    s, e = map(int ,stdin.readline().split())
    visit_graph = [-1] * n
    queue = deque(graph[s - 1])

    visit_graph[s - 1] = 0
    result = 0

    while queue:
        destination, value = queue.popleft()

        if destination == e - 1:
            result += value
            break

        if visit_graph[destination] == -1:
            result += value
            visit_graph[destination] = 0
            for next in graph[destination]:
                queue.append(next)
    print(result)