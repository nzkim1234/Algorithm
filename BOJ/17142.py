from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().split())
virus_startpoints = []
graph = []
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]
base_empty_space = 0

for row in range(n):
    one_line = list(map(int, stdin.readline().split()))

    for col in range(n):
        if one_line[col] == 0:
            base_empty_space += 1
        elif one_line[col] == 2:
            virus_startpoints.append([row, col])
            one_line[col] = -1

    graph.append(one_line)

c_virus_startpoints = list(combinations(virus_startpoints, m))
case = 1
result = 1e9

for virus_startpoint in c_virus_startpoints:
    case += 1
    virus_queue = deque(virus_startpoint)
    virus_queue.append([-1, -1])
    empty_space = base_empty_space
    count = 0
    if empty_space <= 0:
        result = 0
        break
    count += 1

    while virus_queue:
        if count >= result:
            break
        x, y = virus_queue.popleft()

        if empty_space <= 0:
            break

        if [x, y] == [-1, -1]:
            count += 1
            if len(virus_queue) > 0:
                virus_queue.append([-1, -1])
            continue

        if graph[x][y] != case:
            graph[x][y] = case
        
        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < n and 0 <= n_y < n:
                if graph[n_x][n_y] != 1:
                    if graph[n_x][n_y] != case:
                        graph[n_x][n_y] = case
                        if not [n_x, n_y] in virus_startpoints:
                            empty_space -= 1
                        virus_queue.append([n_x, n_y])

    if empty_space <= 0:
        result = min(result, count)

if result == 1e9:
    print(-1)
else:
    print(result)


