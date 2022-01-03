from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())

graph = []

for _ in range(r):
    graph.append(list(stdin.readline().strip()))

position = [[0,1],[1,0],[0,-1],[-1,0]]

queue = deque()
total_sheep = 0
total_wolf = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            queue.append((i, j))
            count_sheep = 0
            count_wolf = 0
            if graph[i][j] == 'v':
                count_wolf += 1
            if graph[i][j] == 'o':
                count_sheep += 1
            while queue:
                y, x = queue.popleft()
                graph[y][x] = '#'
                for v_y, v_x in position:
                    n_y = y + v_y
                    n_x = x + v_x
                    if 0 <= n_y < r and 0 <= n_x < c and graph[n_y][n_x] != '#':
                        queue.append((n_y, n_x))
                        if graph[n_y][n_x] == 'v':
                            count_wolf += 1
                        elif graph[n_y][n_x] == 'o':
                            count_sheep += 1
                        graph[n_y][n_x] = '#'
            
            if count_wolf >= count_sheep:
                total_wolf += count_wolf
            else:
                total_sheep += count_sheep

print(total_sheep, total_wolf)

