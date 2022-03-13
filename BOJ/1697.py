from sys import stdin
from collections import deque

n, k = map(int ,stdin.readline().split())
graph = [1e9] * 100001
queue = deque([[n, 0]])

while queue:
    n, c = queue.popleft()
    graph[n] = min(c, graph[n])
    if 0 <= n + 1 < 100001 and graph[n + 1] > c + 1:
        queue.append([n + 1, c + 1])
    if 0 <= n - 1 < 100001 and graph[n - 1] > c + 1 :
        queue.append([n - 1, c + 1])
    if 0 <= n * 2 < 100001 and graph[n * 2] > c + 1:
        queue.append([n * 2, c + 1])

print(graph[k])