from shutil import move
from sys import stdin

n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
graph = []
count = 0

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

x, y = r, c

while True:
    if graph[x][y] == 0:
        graph[x][y] = 2
        count += 1
    
    moved = False

    for _ in range(4):
        d -= 1
        
        if d < 0:
            d = 3

        n_x = x + direction[d][0]
        n_y = y + direction[d][1]

        if graph[n_x][n_y] == 0:
            x = n_x
            y = n_y
            moved = True
            break

    if not moved:
        n_x = x - direction[d][0]
        n_y = y - direction[d][1]

        if graph[n_x][n_y] == 1:
            break
        else:
            x = n_x
            y = n_y
    
print(count)
    
