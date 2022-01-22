from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
visit_graph = [[0 for _ in range(n)] for _ in range(n)]
rg_visit_graph = [[0 for _ in range(n)] for _ in range(n)]
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
section = 0
red_green_blindness_section = 0

for _ in range(n):
    graph.append(list(map(str, stdin.readline().strip())))
for row in range(n):
    for col in range(n):
        queue = deque()
        rg_queue = deque()
        is_red_green = False

        if visit_graph[row][col] != 1:
            visit_graph[row][col] = 1
            queue.append([row, col])
            section += 1
        
        while queue:
            x, y = queue.popleft()

            for p_x, p_y in position:
                n_x, n_y = x + p_x, y + p_y

                if 0<= n_x < n and 0 <= n_y < n:
                    if visit_graph[n_x][n_y] != 1:
                        if graph[x][y] == graph[n_x][n_y]:
                            visit_graph[n_x][n_y] = 1
                            queue.append([n_x, n_y])

        if rg_visit_graph[row][col] != 1:
            rg_visit_graph[row][col] = 1
            rg_queue.append([row, col])
            red_green_blindness_section += 1
        
        while rg_queue:
            x, y = rg_queue.popleft()

            for p_x, p_y in position:
                n_x, n_y = x + p_x, y + p_y

                if 0<= n_x < n and 0 <= n_y < n:
                    if rg_visit_graph[n_x][n_y] != 1:
                        if graph[x][y] == graph[n_x][n_y] or (graph[x][y] == 'R' and graph[n_x][n_y] =='G') or (graph[x][y] == 'G' and graph[n_x][n_y] =='R'):

                            rg_visit_graph[n_x][n_y] = 1
                            rg_queue.append([n_x, n_y])
                            
print(section, red_green_blindness_section) 