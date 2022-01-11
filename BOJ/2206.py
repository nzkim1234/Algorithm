from sys import stdin
from collections import deque


n, m = map(int, stdin.readline().split())
graph = []
visit_graph = [[[0,0] for _ in range(m)] for _ in range(n)]
visit_graph[0][0][1] = 1
position = [[1, 0], [0, 1], [-1, 0], [0, -1]]
result = -1

for _ in range(n):
    graph.append(list(map(int,list(stdin.readline().strip()))))

queue = deque()
queue.append([0, 0, 1])

while queue:
    x, y, can_break = queue.popleft()

    if [x, y] == [n - 1, m - 1]:
        result = visit_graph[x][y][can_break]
        break

    for p_x, p_y in position:
        n_x = x + p_x
        n_y = y + p_y

        if 0 <= n_x < n and 0 <= n_y < m:
            # 벽이 있고 벽울 부술 수 있는 경우
            if graph[n_x][n_y] == 1 and can_break == 1:
                visit_graph[n_x][n_y][0] =visit_graph[x][y][1] + 1
                queue.append([n_x, n_y, 0])
            # 벽이 없고 이전에 이 칸이 들린 적이 없을 경우
            elif graph[n_x][n_y] == 0 and visit_graph[n_x][n_y][can_break] == 0:
                visit_graph[n_x][n_y][can_break] = visit_graph[x][y][can_break] + 1
                queue.append([n_x,n_y,can_break])

print(result)
