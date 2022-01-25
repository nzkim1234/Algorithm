from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
visit_graph = [[0 for _ in range(n)] for _ in range(n)]  # 일반인 경우의 방문 그래프
rg_visit_graph = [[0 for _ in range(n)] for _ in range(n)]  # 적록색약인 경우의 방문 그래프
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
section = 0
red_green_blindness_section = 0

for _ in range(n):
    graph.append(list(map(str, stdin.readline().strip())))

for row in range(n):
    for col in range(n):
        queue = deque()
        rg_queue = deque()

        # 일반시각의 경우
        if visit_graph[row][col] != 1:  # 방문하지 않았다면 방문 처리, 큐에 추가, 구역 증가
            visit_graph[row][col] = 1
            queue.append([row, col])
            section += 1
        
        # bfs 수행하면서 구역을 전부 방문 표시
        while queue:
            x, y = queue.popleft()

            for p_x, p_y in position:
                n_x, n_y = x + p_x, y + p_y

                if 0<= n_x < n and 0 <= n_y < n:
                    if visit_graph[n_x][n_y] != 1:
                        if graph[x][y] == graph[n_x][n_y]:
                            visit_graph[n_x][n_y] = 1
                            queue.append([n_x, n_y])

        # 적록색약의 경우
        if rg_visit_graph[row][col] != 1:  # 방문하지 않았다면 방문 처리, 큐에 추가, 구역 증가
            rg_visit_graph[row][col] = 1
            rg_queue.append([row, col])
            red_green_blindness_section += 1
        
        # bfs 수행하면서 구역을 전부 방문 표시
        while rg_queue:
            x, y = rg_queue.popleft()

            for p_x, p_y in position:
                n_x, n_y = x + p_x, y + p_y

                if 0<= n_x < n and 0 <= n_y < n:
                    if rg_visit_graph[n_x][n_y] != 1:

                        # 조건에 적록색약 추가
                        if graph[x][y] == graph[n_x][n_y] or (graph[x][y] == 'R' and graph[n_x][n_y] =='G') or (graph[x][y] == 'G' and graph[n_x][n_y] =='R'):
                            rg_visit_graph[n_x][n_y] = 1
                            rg_queue.append([n_x, n_y])
                            
print(section, red_green_blindness_section) 
