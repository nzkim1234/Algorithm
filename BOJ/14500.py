from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

def two_by_three(x, y):
    count = 0
    this_max_num = 0
    list_to_minus = [
        [[x, y], [x, y + 1]], 
        [[x + 1, y + 1], [x + 1, y + 2]], 
        [[x, y], [x + 1, y + 2]], 
        [[x + 1, y], [x + 1, y + 2]], 
        [[x, y], [x, y + 2]],
        [[x, y + 1], [x, y + 2]],
        [[x + 1, y], [x +1, y + 1]],
        [[x + 1, y], [x, y + 2]]
    ]

    for n_x in range(x, x + 2):
        for n_y in range(y, y + 3):
            count += graph[n_x][n_y]

    for position1, position2 in list_to_minus:
        this_max_num = max(this_max_num, count - graph[position1[0]][position1[1]] - graph[position2[0]][position2[1]])
    
    return this_max_num


def three_by_two(x, y):
    count = 0
    this_max_num = 0
    list_to_minus = [
        [[x, y], [x + 1, y]],
        [[x + 1, y + 1], [x + 2, y + 1]], 
        [[x, y], [x + 2, y + 1]], 
        [[x, y + 1], [x + 1, y + 1]], 
        [[x + 1, y], [x + 2, y]], 
        [[x, y + 1], [x + 2, y]], 
        [[x, y + 1], [x + 2, y + 1]], 
        [[x, y], [x + 2, y]]
    ]

    for n_x in range(x, x + 3):
        for n_y in range(y, y + 2):
            count += graph[n_x][n_y]

    for position1, position2 in list_to_minus:
        this_max_num = max(this_max_num, count - graph[position1[0]][position1[1]] - graph[position2[0]][position2[1]])
    
    return this_max_num


def two_by_two(x, y):
    count = 0

    for n_x in range(x, x + 2):
        for n_y in range(y, y + 2):
            count += graph[n_x][n_y]
    
    return count


def four_by_one(x, y):
    count = 0

    for n_x in range(x, x + 4):
        for n_y in range(y, y + 1):
            count += graph[n_x][n_y]
    
    return count


def one_by_four(x, y):
    count = 0

    for n_x in range(x, x + 1):
        for n_y in range(y, y + 4):
            count += graph[n_x][n_y]
    
    return count


max_num = 0

for x in range(n):
    for y in range(m):
        if x + 3 < n:
            max_num = max(max_num, four_by_one(x, y))
        if y + 3 < m:
            max_num = max(max_num, one_by_four(x, y))
        if x + 1 < n and y + 1 < m:
            max_num = max(max_num, two_by_two(x, y))
        if x + 1 < n and y + 2 < m:
            max_num = max(max_num, two_by_three(x, y))
        if x + 2 < n and y + 1 < m:
            max_num = max(max_num, three_by_two(x, y))

print(max_num)