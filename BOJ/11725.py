from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)
result[1] = -1

for _ in range(n - 1):
    s, e = map(int, stdin.readline().split())
    
    graph[s].append(e)
    graph[e].append(s)

queue = deque([1])

while queue:
    node = queue.popleft()

    for e in graph[node]:
        if not result[e]:
            result[e] = node
            queue.append(e)

for i in result[2::]:
    print(i)