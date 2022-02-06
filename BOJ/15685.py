from sys import stdin

graph = [[0 for _ in range(101)] for _ in range(101)]

n = int(stdin.readline())

command = []

for _ in range(n):
    command.append(list(map(int, stdin.readline().split())))

direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
stack = []

for y, x, d, g in command:
    graph[x][y] = 1
    stack = [direction[d]]
    stack2 = [direction[d]]

    for _ in range(g + 1):
        for p_x, p_y in stack2:
            x += p_x
            y += p_y
            graph[x][y] = 1
        stack_range = len(stack)
        stack2 = []
        for i in range(stack_range - 1 , -1, -1):
            new_index = direction.index(stack[i]) + 1
            if new_index > 3:
                new_index = 0
            stack.append(direction[new_index])
            stack2.append(direction[new_index])
        
count = 0
in_range = [[0, 0], [0, 1], [1, 1], [1, 0]]

for x in range(100):
    for y in range(100):
        t_f = True
        for p_x, p_y in in_range:
            n_x = x + p_x
            n_y = y + p_y
            if 0 <= n_x < 101 and 0 <= n_y < 101:
                if graph[n_x][n_y] != 1:
                    t_f = False
                    break
            else:
                break
        if t_f:
            count += 1

print(count)