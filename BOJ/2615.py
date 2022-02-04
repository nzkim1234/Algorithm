from sys import stdin

graph = []

for _ in range(19):
    graph.append(list(map(int, stdin.readline().split())))


def in_a_col(x, y, n):
    count = 0
    for n_x in range(x, 19):
        if 0 <= n_x < 19 and graph[n_x][y] == n:
            count += 1
        else:
            break

    for n_x in range(x, -1, -1):
        if 0 <= n_x < 19 and graph[n_x][y] == n:
            count += 1
        else:
            break
        
    count -= 1

    if count == 5:
        return 1
    else:
        return 0


def in_a_row(x, y, n):
    count = 0
    for n_y in range(y, 19):
        if 0 <= n_y < 19 and graph[x][n_y] == n:
            count += 1
        else:
            break   
    
    for n_y in range(y, -1, -1):
        if 0 <= n_y < 19 and graph[x][n_y] == n:
            count += 1
        else:
            break   
    
    count -= 1

    if count == 5:
        return 1
    else:
        return 0


def in_a_diagonal(x, y, n):
    count = 0
    base = [x, y]

    for _ in range(19):
        if 0<= x < 19 and 0 <= y < 19 and graph[x][y] == n:
            count += 1
        else:
            break
        
        x += 1
        y += 1

    x, y = base

    for _ in range(19):
        if 0<= x < 19 and 0 <= y < 19 and graph[x][y] == n:
            count += 1
        else:
            break
        
        x -= 1
        y -= 1

    count -= 1

    if count == 5:
        return 1
    else:
        return 0


def in_a_diagonal2(x, y, n):
    count = 0
    base = [x, y]

    for _ in range(19):
        if 0<= x < 19 and 0 <= y < 19 and graph[x][y] == n:
            count += 1
        else:
            break
        
        x -= 1
        y += 1

    x, y = base

    for _ in range(19):
        if 0<= x < 19 and 0 <= y < 19 and graph[x][y] == n:
            count += 1
        else:
            break
        
        x += 1
        y -= 1

    count -= 1

    if count == 5:
        return 1
    else:
        return 0


def win():
    for row in range(19):
        for col in range(19):
            if graph[row][col] == 1:
                if in_a_col(row, col, 1) + in_a_row(row, col, 1) + in_a_diagonal(row, col, 1) + in_a_diagonal2(row, col, 1):
                    return [1, row + 1, col + 1]
            elif graph[row][col] ==2:
                if in_a_col(row, col, 2) + in_a_row(row, col, 2) + in_a_diagonal(row, col, 2) + in_a_diagonal2(row,col, 1):
                    return [2, row + 1, col + 1]
    return [0]

result = win()

print(result[0])

if result[0] > 0:
    print(result[1], result[2])