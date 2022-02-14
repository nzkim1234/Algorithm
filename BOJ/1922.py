from sys import stdin
from collections import deque
n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n)]
least_cost_graph = [1e9] * n

for _ in range(m):
    a, b, c = map(int ,stdin.readline().split())
    graph[a - 1].append([b -1, c])
    graph[b - 1].append([a -1, c])

for nodes in graph:
    queue = deque(nodes)
    
    while queue:
        node, value = queue.popleft()
        
