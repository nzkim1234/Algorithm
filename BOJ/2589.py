from sys import stdin
from copy import deepcopy
from collections import deque

n, m = map(int, stdin.readline().split())

graph = []
visit_graph = [[0 for _ in range(m)] for _ in range(n)]
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(n):
    graph.append(list(map(str, list(stdin.readline().strip()))))

count = 1
result = 0
for row in range(n):
    for col in range(m):
        if graph[row][col] == 'L':
            queue = deque([[row, col]])
            queue.append([-1, -1])
            time = -1
            count += 1
            visit_graph[row][col] = count
            while queue:
                x, y = queue.popleft()
                if [x, y] == [-1, -1]:
                    time += 1
                    if queue:
                        queue.append([-1, -1])
                    continue

                for p_x, p_y in position:
                    n_x = x + p_x
                    n_y = y + p_y

                    if 0 <= n_x < n and 0 <= n_y < m:
                        if graph[n_x][n_y] == 'L' and visit_graph[n_x][n_y] != count:
                            visit_graph[n_x][n_y] = count
                            queue.append([n_x, n_y])
            
            result = max(result, time)

print(result)

