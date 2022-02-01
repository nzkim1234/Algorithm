from multiprocessing import connection
from sys import stdin
from itertools import combinations
from collections import deque
from tracemalloc import start
from copy import deepcopy
n, m = map(int, stdin.readline().split())

graph = []
virus_startpoint = []
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]
empty_space = 0

for row in range(n):
    one_line = list(map(int,stdin.readline().split()))
    
    for col in range(n):
        if one_line[col] == 2:
            virus_startpoint.append([row, col])
            one_line[col] = 0
        if one_line[col] == 0:
            empty_space += 1

    graph.append(one_line)

print(empty_space)
virus_startpoint = list(combinations(virus_startpoint, m))
start_num = 1

for start_points in virus_startpoint:
    start_num += 1
    virus_location = deque()
    new_empty_space = empty_space - m

    for x, y in start_points:
        graph[x][y] = start_num
        virus_location.append([x, y])
    
    count = 0
    new_virus_location = deque()
    while virus_location:
        x, y = virus_location.popleft()

        for p_x, p_y in position:
            n_x, n_y = x + p_x, y + p_y
            if 0 <= n_x < n and 0 <= n_y < n:
                if graph[n_x][n_y] != 1 and graph[n_x][n_y] != start_num:
                    graph[n_x][n_y] = start_num
                    new_empty_space -= 1
                    new_virus_location.append([n_x, n_y])

        if not virus_location:
            virus_location = new_virus_location
            new_virus_location = deque()
            count += 1
    print(count)