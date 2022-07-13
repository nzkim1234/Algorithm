from sys import stdin
from collections import deque
from copy import deepcopy

n, m = map(int ,stdin.readline().split())
graph = []
position = [[0, 1], [0, -1], [1, 0], [-1, 0]]
result = 0

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))


def bfs():
    global result
    queue = deque()
    new_graph = deepcopy(graph)

    for x in range(n):
        for y in range(m):
            if new_graph[x][y] == 2:
                queue.append([x, y])
    
    while queue:
        c_x, c_y = queue.popleft()

        for p_x, p_y in position:
            n_x = c_x + p_x
            n_y = c_y + p_y

            if 0 <= n_x < n and 0 <= n_y < m:
                if new_graph[n_x][n_y] == 0:
                    new_graph[n_x][n_y] = 2
                    queue.append([n_x, n_y])
    
    current_result = 0

    for i in range(n):
        current_result += new_graph[i].count(0)
    
    result = max(result, current_result)


def make_wall(num):
    if num == 3:
        bfs()
        return
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                graph[x][y] = 1
                make_wall(num + 1)
                graph[x][y] = 0


make_wall(0)

print(result)
