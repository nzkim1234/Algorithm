from sys import stdin
from collections import deque

n, m, k = map(int, stdin.readline().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    y, x = map(int, stdin.readline().split())

    graph[y - 1][x - 1] = 1

queue = deque()

position = [[0,1],[1,0],[0,-1],[-1,0]]
big_trash = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            trash_size = 0
            graph[i][j] = 0
            queue.append([i, j])

            while queue:
                trash_size += 1
                y, x = queue.popleft()

                for v_y, v_x in position:
                    n_y = y + v_y
                    n_x = x + v_x
                    if 0 <= n_y < n and 0 <= n_x < m and graph[n_y][n_x] != 0:
                        graph[n_y][n_x] = 0
                        queue.append([n_y, n_x])

            big_trash =max(big_trash, trash_size)

print(big_trash)
