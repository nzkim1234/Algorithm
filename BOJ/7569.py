from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())

graph = [[] for _ in range(h)]
loc_tomato = []
count_0 = 0
for i in range(h):
    for j in range(n):
        indexs = list(map(int, stdin.readline().split()))
        
        for k in range(m):
            if indexs[k] == 1:
                loc_tomato.append([i, j, k])
            if indexs[k] == 0:
                count_0 += 1
        
        graph[i].append(indexs)

time = 0
queue = deque(loc_tomato)
queue.append([-1, -1, -1])
position = [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]

while queue:
    s_h, s_x, s_y = queue.popleft()
    if s_h + s_x + s_y < 0:
        if queue:
            time += 1
            queue.append([-1, -1, -1])
    
    for p_h, p_x, p_y in position:
        n_h, n_x, n_y = s_h + p_h, s_x + p_x, s_y + p_y
        
        if (0 <= n_h < h) and (0 <= n_x < n) and (0 <= n_y < m):
            if graph[n_h][n_x][n_y] == 0:
                count_0 -= 1
                graph[n_h][n_x][n_y] = 1
                queue.append([n_h, n_x, n_y])

if count_0:
    print(-1)
else:
    print(time)
