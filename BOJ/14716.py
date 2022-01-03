from sys import stdin
from collections import deque

graph = []
m, n = map(int, stdin.readline().split())
queue = deque()
result = 0
near_by = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]  # 인접한 칸 

for _ in range(m):
    graph.append(list(map(int, stdin.readline().split())))

for i in range(m):
    for j in range(n):
        if graph[i][j]:
            result += 1
            graph[i][j] = 0
            queue.append([i, j])

            # bfs을 돌면서 값이 1 일시 0으로 바꾸기 
            while queue:
                x, y = queue.popleft()

                for p_x, p_y in near_by:
                    n_x = x + p_x
                    n_y = y + p_y

                    if 0 <= n_x < m and 0 <= n_y < n:
                        if  graph[n_x][n_y]:
                            graph[n_x][n_y] = 0
                            queue.append([n_x, n_y])

print(result)