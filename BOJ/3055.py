from sys import stdin

r, c = map(int, stdin.readline().split())

graph = []
destination = []
start_point = []
water_point = []
stone_point = []
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for i in range(r):
    one_row = list(map(str,stdin.readline().strip()))
    for j in range(len(one_row)):
        if one_row[j] == 'D':
            destination = [i, j]
        elif one_row[j] == 'S':
            start_point.append([i, j])
        elif one_row[j] == '*':
            water_point.append([i, j])
        elif one_row[j] == 'X':
            stone_point.append([i, j])
    graph.append(one_row)

count = 0

while True:
    count += 1
    new_water_point = []
    new_start_point = []
    for x, y in water_point:
        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < r and 0 <= n_y < c:
                if graph[n_x][n_y] != 'X' and graph[n_x][n_y] != 'D' and graph[n_x][n_y] != '*' and not [n_x, n_y] in new_water_point:
                    graph[n_x][n_y] = '*'
                    new_water_point.append([n_x, n_y])

    water_point = new_water_point

    if not start_point:
        print('KAKTUS')
        break

    for x, y in start_point:
        graph[x][y] = '~'
        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < r and 0 <= n_y < c:
                if graph[n_x][n_y] != 'X' and graph[n_x][n_y] != '*' and graph[n_x][n_y] != '~' and not [n_x, n_y] in new_start_point:
                    graph[n_x][n_y] = 'S'
                    new_start_point.append([n_x, n_y])
        
    start_point = new_start_point

    if destination in start_point:
        print(count)
        break