from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

graph = []
visit_graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    line = list(map(int, map(str, stdin.readline().strip())))
    graph.append(line)

position = [[0, 1], [-1, 0], [0, -1], [1, 0]]
queue = deque([[0, 0]])
queue.append([-1, -1])
visit_graph[0][0] = 1
count = 1

while queue:
    x, y = queue.popleft()

    if x == -1 and y == -1 and queue:
        queue.append([-1, -1])
        count += 1
        continue

    for p_x, p_y in position:
        n_x = x + p_x
        n_y = y + p_y

        if 0 <= n_x < n and 0 <= n_y < m:
            if not visit_graph[n_x][n_y] and graph[n_x][n_y] == 1:
                queue.append([n_x, n_y])
                visit_graph[n_x][n_y] = count
    

print(visit_graph[n-1][m-1] + 1)

