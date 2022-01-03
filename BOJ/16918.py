from sys import stdin
from copy import deepcopy
r, c, n = map(int,stdin.readline().split())
graph = []
only_bomb_graph = [['O' for _ in range(c)] for _ in range(r)]
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(r):
    graph.append(list(stdin.readline().strip()))

time = 0


time += 1

while time < n:
    time += 1
    case = time % 2

    if case == 1:   
         for x, y in bomb_location:
            graph[x][y] = '.'

            for p_x, p_y in position:
                n_x = x + p_x
                n_y = y + p_y

                if 0 <= n_x < r and 0 <= n_y < c:
                    if graph[n_x][n_y] == 'O':
                        graph[n_x][n_y] = '.'

    else:
        bomb_location = []

        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    bomb_location.append([i, j])

        graph = deepcopy(only_bomb_graph)
       
for i in graph:
        print(''.join(i))