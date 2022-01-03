from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
position = [[1, 0],[0, 1], [-1, 0], [0, -1]]
queue = deque()
result = 0
result_list = []

for _ in range(n):
    graph.append(list(stdin.readline()))

# 그래프를 탐색하면서 1을 찾을시 bfs을 돌려 단지를 구한다
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            result += 1
            count = 0
            queue.append([i, j])
            graph[i][j] = '0'

            while queue:
                count += 1
                x, y = queue.pop()

                for p_x, p_y in position:
                    n_x = x + p_x
                    n_y = y + p_y
                    
                    if 0 <= n_x < n and 0 <= n_y < n:
                        if graph[n_x][n_y] == '1':
                            queue.append([n_x, n_y])
                            graph[n_x][n_y] = '0'

            result_list.append(count)

result_list.sort()

print(result)

for i in result_list:
    print(i)
