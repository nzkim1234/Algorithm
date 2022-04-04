from sys import stdin

n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
direction = [[-1, 0], [0, 1], [1, 0], [-1, 0]]
graph = []
count = 0

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

x, y = r, c
while True:
    graph[x][y] = 2
    print(graph)
    count += 1
    for _ in range(4):
        d -= 1
        if d < 0:
            d = 3
        
        n_x = x + direction[d][0]
        n_y = y + direction[d][1]

        if 0 <= n_x < n and 0 <= n_y < m:
            if graph[n_x][n_y] == 0:
                x = n_x
                y = n_y
                continue
    
    d = (d + 2) % 4

    n_x = x + direction[d][0]
    n_x = y + direction[d][1]
    print(n_x, n_y)
    print(graph[n_x][n_y])
    if graph[n_x][n_y] == 1:
        break
    else:
        x = n_x
        y = n_y
