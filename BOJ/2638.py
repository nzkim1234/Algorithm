from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = []
time = 0
position = [[0, 1], [1, 0], [0, -1], [-1, 0]]
queue = deque()
result = 0

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

while True:
    visit_graph = [[True for _ in range(m)] for _ in range(n)]
    visit_graph[0][0] = False
    queue.append([0, 0])
    melt_cheese = []

    # bfs 탐색을 하면서 치즈로 둘러 쌓여있는 부분이 아닌 부분을 찾기
    while queue:
        x, y = queue.popleft()

        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y
            if 0 <= n_x < n and 0 <= n_y < m:
                if graph[n_x][n_y] == 0 and visit_graph[n_x][n_y] == True:
                    visit_graph[n_x][n_y] = False
                    queue.append([n_x, n_y])

    # visit_graph를 탐색하며서 True일 경우 상하좌우에 공기가 2개 이상일 경우 melt_cheese에 좌표값을 추가
    for x in range(n):
        for y in range(m):
            if visit_graph[x][y] == True:
                count = 0

                for p_x, p_y in position:
                    n_x = x + p_x
                    n_y = y + p_y
                    if 0 <= n_x < n and 0 <= n_y < m:
                        if visit_graph[n_x][n_y] == False:
                            count += 1

                if count >= 2:
                    melt_cheese.append([x, y])

    if not melt_cheese:  # 녹는 치즈가 없을 경우 break
        break

    # melt_cheese에서 좌표를 가져와 치즈 녹이기
    for x, y in melt_cheese:
        graph[x][y] = 0

    result += 1

print(result)