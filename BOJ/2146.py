from sys import stdin
from collections import deque


def find_island(i, j, start_num):
    global answer
    result = 1
    queue = deque()
    queue.append([i, j])
    queue.append([-1, -1])

    while queue:
        x, y = queue.popleft()

        if result >= answer:
            break
        
        if x == -1 and y == -1:
            result += 1

            if queue:
                queue.append([-1, -1])

            continue
        
        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < n and 0 <= n_y < n:
                if graph[n_x][n_y] != start_num:
                    if graph[n_x][n_y] == 0:
                        queue.append([n_x, n_y])

                    elif graph[n_x][n_y] != start_num:
                        answer = result
                        

n = int(stdin.readline())
graph = []
visit_graph = [[False for _ in range(n)] for _ in range(n)]
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]
num = 1
answer = 1e9

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

for x in range(n):
    for y in range(n):
        if not visit_graph[x][y]and graph[x][y] == 1:
            num += 1
            queue = deque()
            queue.append([x, y])
            visit_graph[x][y] = True
            graph[x][y] = num

            while queue:
                c_x, c_y = queue.popleft()

                for p_x, p_y in position:
                    n_x = p_x + c_x
                    n_y = p_y + c_y

                    if 0 <= n_x < n and 0 <= n_y < n:
                        if not visit_graph[n_x][n_y]  and graph[n_x][n_y] == 1:
                            visit_graph[n_x][n_y] = True
                            graph[n_x][n_y] = num
                            queue.append([n_x, n_y])

for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            for p_x, p_y in position:
                n_x = x + p_x
                n_y = y + p_y
                
                if 0 <= n_x < n and 0 <= n_y < n:
                    if not graph[n_x][n_y]:
                        find_island(n_x, n_y, graph[x][y])

print(answer)
