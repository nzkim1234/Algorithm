from sys import stdin

n = int(stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(str,stdin.readline().strip())))

position = [[0, 1], [1, 0]]
result = 0

for i in range(n):
    for j in range(n):
        for p_x, p_y in position:
            n_x = i + p_x
            n_y = j + p_y
            current_result = 0

            if 0<= n_x < n and 0 <= n_y < n:
                if graph[i][j] != graph[n_x][n_y]:
                    graph[i][j], graph[n_x][n_y] = graph[n_x][n_y], graph[i][j]
                    
                    
                    for x in range(n):
                        current_result = 0
                        start = graph[x][0]
                        for y in range(n):
                            if graph[x][y] == start:
                                current_result += 1
                            else:
                                if result < current_result:
                                    result = current_result
                                current_result = 1
                                start = graph[x][y]
                            if result < current_result:
                                result = current_result

                    for y in range(n):
                        current_result = 0
                        start = graph[0][y]
                        for x in range(n):
                            if graph[x][y] == start:
                                current_result += 1
                            else:
                                if result < current_result:
                                    result = current_result
                                current_result = 1
                                start = graph[x][y]
                        if result < current_result:
                            result = current_result

                    graph[i][j], graph[n_x][n_y] = graph[n_x][n_y], graph[i][j]

print(result)
