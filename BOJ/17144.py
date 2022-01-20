from sys import stdin

r, c, t = map(int, stdin.readline().split())
graph = []
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]
aircleaner = []
for row in range(r):
    graph.append([])
    for dust in list(map(int, stdin.readline().split())):
        graph[row].append([dust, 0])
        if dust == -1:
            aircleaner.append([row, graph[row].index([dust, 0])])

for _ in range(t):
    
    for i in range(r):
        for j in range(c):
            if graph[i][j][0] > 0:
                count = 0
                
                for p_x, p_y in position:
                    n_x, n_y = i + p_x, j + p_y
                    if 0 <= n_x < r and 0 <= n_y < c:
                        if graph[n_x][n_y][0] != -1:
                            count += 1
                            graph[n_x][n_y][1] += graph[i][j][0] // 5
                
                graph[i][j][0] = graph[i][j][0] - (graph[i][j][0] // 5 * count)

    for i in range(r):
        for j in range(c):
            if graph[i][j][1] != 0:
                graph[i][j][0] += graph[i][j][1]
                graph[i][j][1] = 0

    rorate = 0
    air_x = aircleaner[0][0]
    air_y = aircleaner[0][1]
    storage = -1

    while True:
        if rorate == 0:
            if 0 <= air_y + 1 < c:
                air_y += 1
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]
                storage = new_storage
            else:
                rorate += 1

        elif rorate == 1:
            if 0 <= air_x - 1 < r:
                air_x -= 1
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = 0
                storage = new_storage
            else:
                rorate += 1
        elif rorate == 2:
            if 0 <= air_y - 1 < c:
                air_y -= 1
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = 0
                storage = new_storage
            else:
                rorate += 1

        elif rorate == 3:
            if 0 <= air_x + 1 < r:
                air_x += 1
                if [air_x, air_y] == aircleaner[0]:
                    break
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = 0
                storage = new_storage
            else:
                break

    rorate = 0
    air_x = aircleaner[1][0]
    air_y = aircleaner[1][1]
    storage = -1


    while True:
        if rorate == 0:
            if 0 <= air_y + 1 < c:
                air_y += 1
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]
                storage = new_storage
            else:
                rorate += 1

        elif rorate == 1:
            if 0 <= air_x + 1 < r:
                air_x += 1
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = 0
                storage = new_storage
            else:
                rorate += 1
        elif rorate == 2:
            if 0 <= air_y - 1 < c:
                air_y -= 1
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = 0
                storage = new_storage
            else:
                rorate += 1

        elif rorate == 3:
            if 0 <= air_x - 1 < r:
                air_x -= 1
                if [air_x, air_y] == aircleaner[1]:
                    break
                new_storage = graph[air_x][air_y]
                if storage != -1:
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = 0
                storage = new_storage
            else:
                break

result = 0

for i in graph:
    for j in i:
        result += j[0]
print(result + 2)