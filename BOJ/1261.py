from sys import stdin
from collections import deque


n, m = map(int, stdin.readline().split())

graph = []
count_graph = [[1e9 for _ in range(n)] for _ in range(m)]
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(m):
    graph.append(list(map(int, map(str ,stdin.readline().strip()))))

count_graph[0][0] = 0
queue = deque([[0, 0]])

while queue:
    x, y = queue.popleft()

    for p_x, p_y in position:
        n_x = x + p_x
        n_y = y + p_y

        if 0 <= n_x < m and 0 <= n_y < n:
            current_count = count_graph[x][y] + graph[n_x][n_y]
            
            if count_graph[n_x][n_y] > current_count:
                count_graph[n_x][n_y] = current_count
                queue.append([n_x, n_y])

print(count_graph[m - 1][n - 1])